import argparse
from typing import NoReturn
from game import Game

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []
        self.tractor1_done = False
        self.tractor2_done = False
        self.tractor3_done = False
        self.tractor4_done = False
        self.tractor5_done = False
        self.game = Game()

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            game_data: dict = self.read_json()
            for farm in game_data["farms"]:
                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            farms = my_farm
            fields = farms["fields"]
            farmers = farms["employees"]

            if game_data["day"] == 0:
                self.game.add_command("0 EMPRUNTER 250000")
                for _ in range(5):
                    self.game.add_command("0 ACHETER_CHAMP")
                for _ in range(5):
                    self.game.add_command("0 ACHETER_TRACTEUR")
                for _ in range(1, 39):
                    self.game.add_command("0 EMPLOYER")
                self.game.distribute_sawer()
                self.game.distribute_farmers()
                self.game.distribute_cook()

            if game_data["day"] >= 5:
                self.game.saw(fields=fields)
                for farmer in farmers:
                    for field in fields:
                        if field["location"] == "FIELD1":
                            self.game.water(
                                need_water_1=field["needed_water"],
                                need_water_2=3,
                                need_water_3=3,
                                need_water_4=3,
                                need_water_5=3,
                                farmer_id=farmer["id"],
                                farmer_location=farmer["location"],
                            )
                            self.tractor1_done = self.game.stocker_field1(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock_done=self.tractor1_done,
                            )
                        if field["location"] == "FIELD2":
                            self.tractor2_done = self.game.stocker_field2(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock_done=self.tractor2_done,
                            )
                        if field["location"] == "FIELD3":
                            self.tractor3_done = self.game.stocker_field3(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock_done=self.tractor3_done,
                            )
                        if field["location"] == "FIELD4":
                            self.tractor4_done = self.game.stocker_field4(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock_done=self.tractor4_done,
                            )
                        if field["location"] == "FIELD5":
                            self.tractor5_done = self.game.stocker_field5(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock_done=self.tractor5_done,
                            )
            if game_data["day"] >= 30:
                self.game.cook()

            #if game_data["day"] == 60:
            #    self.game.fire()
            #    for _ in range(1, 39):
            #        self.game.add_command("0 EMPLOYER")
            #    self.game.distribute_sawer()
            #    self.game.distribute_farmers()
            #    self.game.distribute_cook()
            
            self.send_commands()

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self.game.commands}
        print("sending", data)
        self.send_json(data)
        self.game.commands.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=16210,
    )

    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port, "Ferme").run()

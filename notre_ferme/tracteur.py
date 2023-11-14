import argparse

from typing import NoReturn
from notre_ferme.game import Game

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []
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
            print(game_data["day"])

            farms = my_farm
            fields_json = farms["fields"]
            self.game.update_fields(fields_json)
            farmers = farms["employees"]
            soup_factory = farms["soup_factory"]

            if game_data["day"] == 0:
                self.game.add_command("0 EMPRUNTER 150000")
                for _ in range(5):
                    self.game.add_command("0 ACHETER_CHAMP")
                for _ in range(5):
                    self.game.add_command("0 ACHETER_TRACTEUR")
                for _ in range(1, 38):
                    self.game.add_command("0 EMPLOYER")
                self.game.distribute_sawer(fields=fields_json)
                self.game.distribute_farmers()
                self.game.distribute_cook()

            if game_data["day"] == 8:
                for field in fields_json:
                    if field["location"] == "FIELD1":
                        self.game.sell(need_water=field["needed_water"])

            if (
                5 <= game_data["day"] < 480
                or 485 <= game_data["day"] < 960
                or 965 <= game_data["day"] < 1440
                or game_data["day"] >= 1445
            ):
                self.game.saw(fields=fields_json, stock=soup_factory["stock"])
                for farmer in farmers:
                    for field in fields_json:
                        if field["location"] == "FIELD1":
                            self.game.water(
                                need_water_1=field["needed_water"],
                                need_water_2=3,
                                need_water_3=3,
                                need_water_4=3,
                                need_water_5=3,
                                farmer_id=farmer["id"],
                            )
                            if game_data["day"] > 8:
                                self.game.stocker_field1(
                                    content=field["content"],
                                    need_water=field["needed_water"],
                                    farmer_id=farmer["id"],
                                    farmer_pos=farmer["location"],
                                )
                        if field["location"] == "FIELD2":
                            self.game.stocker_field2(
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                            )
                        if field["location"] in ("FIELD3", "FIELD4", "FIELD5"):
                            self.game.stocker_field3_4_5(
                                field_pos=field["location"],
                                content=field["content"],
                                need_water=field["needed_water"],
                                farmer_id=farmer["id"],
                                farmer_pos=farmer["location"],
                                stock=soup_factory["stock"],
                            )
            if (
                5 <= game_data["day"] < 480
                or 486 <= game_data["day"] < 960
                or 966 <= game_data["day"] < 1440
                or game_data["day"] >= 1446
            ):
                self.game.cook(stock=soup_factory["stock"])

            if (
                game_data["day"] == 480
                or game_data["day"] == 960
                or game_data["day"] == 1440
            ):
                self.game.fire()
                for _ in range(1, 36):
                    self.game.add_command("0 EMPLOYER")
                if game_data["day"] == 480:
                    self.game.team = 1
                if game_data["day"] == 960:
                    self.game.team = 2
                if game_data["day"] == 1440:
                    self.game.team = 3
                self.game.distribute_sawer_2(fields=fields_json)
                self.game.distribute_farmers()
                self.game.distribute_cook()

            if game_data["day"] == 1441:
                for _ in range(1, 6):
                    self.game.add_command("0 EMPLOYER")
                self.game.end_game()

            if game_data["day"] >= 1447:
                self.game.cook_end(stock=soup_factory["stock"])

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

    client = PlayerGameClient(args.address, args.port, "Tracteur").run()

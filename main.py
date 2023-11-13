#4 014 966

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
            #print(my_farm)
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
                for _ in range(1, 40):
                    self.game.add_command("0 EMPLOYER")
                self.game.distribute_sawer(fields=fields_json)
                self.game.distribute_farmers()
                self.game.distribute_cook()

            if (
                5 <= game_data["day"] < 200
                or 205 <= game_data["day"] < 400
                or 405 <= game_data["day"] < 600
                or 605 <= game_data["day"] < 800
                or 805 <= game_data["day"] < 1000
                or 1005 <= game_data["day"] < 1200
                or 1205 <= game_data["day"] < 1400
                or 1405 <= game_data["day"] < 1600
                or game_data["day"] >= 1605
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
                            if game_data["day"] < 1795:
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
                            )
            if (
                5 <= game_data["day"] < 200
                or 206 <= game_data["day"] < 400
                or 406 <= game_data["day"] < 600
                or 606 <= game_data["day"] < 800
                or 806 <= game_data["day"] < 1000
                or 1006 <= game_data["day"] < 1200
                or 1206 <= game_data["day"] < 1400
                or 1406 <= game_data["day"] < 1600
                or game_data["day"] >= 1605
            ):
                self.game.cook(stock=soup_factory["stock"])

            if game_data["day"] == 200:
                self.game.team = 1

            if game_data["day"] == 400:
                self.game.team = 2

            if game_data["day"] == 600:
                self.game.team = 3

            if game_data["day"] == 800:
                self.game.team = 4

            if game_data["day"] == 1000:
                self.game.team = 5

            if game_data["day"] == 1200:
                self.game.team = 6

            if game_data["day"] == 1400:
                self.game.team = 7

            if game_data["day"] == 1600:
                self.game.team = 8

            if (
                game_data["day"] == 200
                or game_data["day"] == 400
                or game_data["day"] == 600
                or game_data["day"] == 800
                or game_data["day"] == 1000
                or game_data["day"] == 1200
                or game_data["day"] == 1400
                or game_data["day"] == 1600

            ):
                self.game.fire()
                for _ in range(1, 38):
                    self.game.add_command("0 EMPLOYER")
                self.game.distribute_sawer_2(fields=fields_json)
                self.game.distribute_farmers()
                self.game.distribute_cook()

            if game_data["day"] == 1441:
                for _ in range(1, 5):
                    self.game.add_command("0 EMPLOYER")
                self.game.end_game()

            if game_data["day"] >= 1447:
                self.game.cook_end(stock=soup_factory["stock"])

            if game_data["day"] >= 1795:
                self.game.add_command("1 CUISINER")

            if game_data["day"] == 1797:
                self.game.sell(need_water=field["needed_water"])

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

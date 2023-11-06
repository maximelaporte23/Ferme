import argparse
from typing import NoReturn
from vegetable import Vegetable
from location import Location
from field import Field
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
            print(my_farm)

            farms = my_farm
            fields = farms["fields"]
            soup_factory = farms["soup_factory"]
            farmers = farms["employees"]

            if game_data["day"] == 0:
                self.game.add_command("0 EMPRUNTER 150000")
                for _ in range(5):
                    self.game.add_command("0 ACHETER_CHAMP")
                for _ in range(36):
                    self.game.add_command("0 EMPLOYER")
                for _ in range(3):
                    self.game.add_command("0 ACHETER_TRACTEUR")
                for sprinkler in range(1, 26):
                    champ = ((sprinkler - 1) % 5) + 1
                    self.game.add_command(f"{sprinkler} ARROSER {champ}")
                for seeder in range(26, 31):
                    champ = ((seeder - 1) % 5) + 1
                    self.game.add_command(f"{seeder} SEMER POIREAU {champ}")
                for cook in range(32, 37):
                    self.game.add_command(f"{cook} CUISINER")

            if game_data["day"] >= 5:
                self.game.saw(fields=fields)
                self.game.cook(stock=soup_factory["stock"])
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

            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self.game.commands.append(command)

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

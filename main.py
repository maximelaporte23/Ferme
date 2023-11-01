import argparse
from typing import NoReturn
from vegetable import Vegetable
from location import Location
from field import Field

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

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

            farms = my_farm
            fields = farms["fields"]
            soup_factory = farms["soup_factory"]
            farmers = farms["employees"]

            print(type(fields), fields)

#             if game_data["day"] == 0:
#                 self.add_command("0 EMPRUNTER 300000")
#                 for _ in range(5):
#                     self.add_command("0 ACHETER_CHAMP")
#                 for _ in range(36):
#                     self.add_command("0 EMPLOYER")
#                 for _ in range(3):
#                     self.add_command("0 ACHETER_TRACTEUR")
#                 self.add_command("27 SEMER PATATE 3")
#                 self.add_command("28 SEMER PATATE 4")
#                 for OUVRIER in range(1, 26):
#                     CHAMP = ((OUVRIER - 1) % 5) + 1
#                     self.add_command("{OUVRIER} ARROSER {CHAMP}")
#                 for OUVRIER in range(32, 37):
#                     self.add_command(f"{OUVRIER} CUISINER")
            
#             for field in game_data["fields"]:
#                 if Location.fields[0] == Vegetable.NONE:
#                     next_vegetable = Vegetable(self.vegetable_index)
#                     self.add_command(f"26 SEMER {next_vegetable.name} 1")
#                     self.vegetable_index = (self.vegetable_index + 1) % len(Vegetable)
            
#             if game_data["day"] >= 2:
#                 for OUVRIER in range(1, 6):
#                     self.add_command(f"{OUVRIER} ARROSER 1")
#             if game_data["day"] >= 3:
#                 for OUVRIER in range(6, 11):
#                     self.add_command(f"{OUVRIER} ARROSER 2")
#             if game_data["day"] >= 4:
#                 for OUVRIER in range(11, 16):
#                     self.add_command(f"{OUVRIER} ARROSER 3")
#             if game_data["day"] >= 5:
#                 for OUVRIER in range(16, 21):
#                     self.add_command(f"{OUVRIER} ARROSER 4")
#             if game_data["day"] >= 6:
#                 for OUVRIER in range(21, 26):
#                     self.add_command(f"{OUVRIER} ARROSER 5")
            

# for OUVRIER in range(1, 26):
#                     CHAMP = ((OUVRIER - 1) % 5) + 1
#                     self.add_command("{OUVRIER} ARROSER {CHAMP}")
#             self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        # print("sending", data)
        self.send_json(data)
        self._commands.clear()


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
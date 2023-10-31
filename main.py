import argparse
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            game_data = self.read_json()
            for farm in game_data["farms"]:
                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            if game_data["day"] == 0:
                self.add_command("0 EMPRUNTER 300000")
                for _ in range(5):
                    self.add_command("0 ACHETER_CHAMP")
                for _ in range(31):
                    self.add_command("0 EMPLOYER")
                for _ in range(3):
                    self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("26 SEMER OIGNON 1")
                for OUVRIER in range(1, 6):
                    self.add_command(f"{OUVRIER} ARROSER {1}")
                for OUVRIER in range(6, 11):
                    self.add_command(f"{OUVRIER} ARROSER {2}")
                for OUVRIER in range(11, 16):
                    self.add_command(f"{OUVRIER} ARROSER {3}")
                for OUVRIER in range(16, 21):
                    self.add_command(f"{OUVRIER} ARROSER {4}")
                for OUVRIER in range(21, 26):
                    self.add_command(f"{OUVRIER} ARROSER {5}")
            
            if game_data["day"] >= 1:
                if game_data["day"] == 1:
                    self.add_command("26 SEMER PATATE 2")
                if game_data["day"] == 2:
                    self.add_command("26 SEMER TOMATE 3")
                if game_data["day"] == 3:
                    self.add_command("26 SEMER POIREAU 4")
                    for OUVRIER in range(1, 6):
                        self.add_command(f"{OUVRIER} ARROSER {1}")
                    self.add_command("27 STOCKER 1 1")
                if game_data["day"] == 4:
                    self.add_command("26 SEMER COURGETTE 5")
                    for OUVRIER in range(6, 11):
                        self.add_command(f"{OUVRIER} ARROSER {2}")
                    self.add_command("28 STOCKER 2 2")
                if game_data["day"] == 5:
                    for OUVRIER in range(11, 16):
                        self.add_command(f"{OUVRIER} ARROSER {3}")
                    self.add_command("29 STOCKER 3 3")
                if game_data["day"] == 6:
                    for OUVRIER in range(16, 21):
                        self.add_command(f"{OUVRIER} ARROSER {4}")
                    self.add_command("27 STOCKER 4 1")        
                if game_data["day"] == 8:
                    for OUVRIER in range(21, 26):
                        self.add_command(f"{OUVRIER} ARROSER {5}")
                    self.add_command("28 STOCKER 5 2")
                if 9 <= game_data["day"] <= 29:
                    self.add_command("31 CUISINER")  
            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
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
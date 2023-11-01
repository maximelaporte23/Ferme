class Game:
    def __init__(self: "Game") -> None:
        self.commands = []
        self.farmer = []
        self.fields = []

    def cook(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            for OUVRIER in range(31, 36):
                    self.add_command(f"{OUVRIER} CUISINER")

    def distribute_sawer(self):
        self.add_command("26 SEMER POIREAU 1")
        self.add_command("27 SEMER POIREAU 2")
        self.add_command("28 SEMER POIREAU 2")
        self.add_command("29 SEMER POIREAU 4")
        self.add_command("30 SEMER POIREAU 5")
    
    def saw(self, fields):
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        for i in range(len(fields)):
            field = fields[i]
            vegetable_to_seed = vegetables[i % len(vegetables)]
            if field["content"] == "NONE":
                self.add_command(f"{26 + i} SEMER {vegetable_to_seed} {i + 1}")
    
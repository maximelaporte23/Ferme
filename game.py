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
    
    def water(
        self,
        need_water_1,
        need_water_2,
        need_water_3,
        need_water_4,
        need_water_5,
        farmer_id,
        farmer_location,
    ):
        if need_water_1 != 0:
            if farmer_id <= 5:
                self.add_command(f"{farmer_id} ARROSER 1")
        if need_water_2 != 0:
            if farmer_id > 5 and farmer_id <= 10:
                self.add_command(f"{farmer_id} ARROSER 2")
        if need_water_3 != 0:
            if farmer_id > 10 and farmer_id <= 15:
                self.add_command(f"{farmer_id} ARROSER 3")
        if need_water_4 != 0:
            if farmer_id > 15 and farmer_id <= 20:
                self.add_command(f"{farmer_id} ARROSER 4")
        if need_water_5 != 0:
            if farmer_id > 20 and farmer_id <= 25:
                self.add_command(f"{farmer_id} ARROSER 5")
    
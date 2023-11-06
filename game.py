class Game:
    def __init__(self: "Game") -> None:
        self.commands = []
        self.farmer = []
        self.fields = []
        self.vegetable_index = 0

    def hire_farmers(self, nb_farmers):
        for _ in range(nb_farmers):
            self.add_command("0 EMPLOYER")

    def hire_sawer(self, nb_sawers):
        for _ in range(nb_sawers):
            self.add_command("0 EMPLOYER")

    def distribute_sawer(self):
        self.add_command("35 SEMER POIREAU 1")
        self.add_command("36 SEMER POIREAU 2")
        self.add_command("37 SEMER POIREAU 2")
        self.add_command("38 SEMER POIREAU 4")
        self.add_command("39 SEMER POIREAU 5")

    def distribute_farmers(self, nb_employees, nb_of_cook, nb_of_stocker):
        farmer_num = 0
        for field_num in range(1, 6):
            for _ in range(5):
                farmer_num += 1
                self.add_command(f"{farmer_num} SEMER PATATE {field_num}")
                if farmer_num >= nb_employees - nb_of_cook - nb_of_stocker:
                    return

    def cook(self, stock):
        if (
            stock["POTATE"] != 0
            and stock["COURGETTE"] != 0
            and stock["TOMATE"] != 0
            and stock["OIGNON"] != 0
            and stock["POIREAU"] != 0
        ):
            for OUVRIER in range(31, 36):
                self.add_command(f"{OUVRIER} CUISINER")

    def saw(self, fields):
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        vegetable_to_seed = vegetables[self.vegetable_index]

        field1 = fields[0]
        field2 = fields[1]
        field3 = fields[2]
        field4 = fields[3]
        field5 = fields[4]
        if field1["content"] == "NONE":
            self.add_command(f"35 SEMER {vegetable_to_seed} 1")
        if field2["content"] == "NONE":
            self.add_command(f"36 SEMER {vegetable_to_seed} 2")
        if field3["content"] == "NONE":
            self.add_command(f"37 SEMER {vegetable_to_seed} 3")
        if field4["content"] == "NONE":
            self.add_command(f"38 SEMER {vegetable_to_seed} 4")
        if field5["content"] == "NONE":
            self.add_command(f"39 SEMER {vegetable_to_seed} 5")

        self.vegetable_index = (self.vegetable_index + 1) % len(vegetables)

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
       
    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

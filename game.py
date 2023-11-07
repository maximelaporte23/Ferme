class Game:
    def __init__(self: "Game") -> None:
        self.commands = []
        self.farmer = []
        self.fields = []
        self.vegetable_index = 0

    def distribute_farmers(self):
        for farmer_num in range(1, 6):
            self.add_command(f"{farmer_num} ARROSER 1")
        for farmer_num in range(6, 11):
            self.add_command(f"{farmer_num} ARROSER 2")
        for farmer_num in range(11, 16):
            self.add_command(f"{farmer_num} ARROSER 3")
        for farmer_num in range(16, 21):
            self.add_command(f"{farmer_num} ARROSER 4")
        for farmer_num in range(21, 26):
            self.add_command(f"{farmer_num} ARROSER 5")

    def distribute_farmers_2(self):
        for farmer_num in range(40, 45):
            self.add_command(f"{farmer_num} ARROSER 1")
        for farmer_num in range(45, 50):
            self.add_command(f"{farmer_num} ARROSER 2")
        for farmer_num in range(50, 55):
            self.add_command(f"{farmer_num} ARROSER 3")
        for farmer_num in range(55, 60):
            self.add_command(f"{farmer_num} ARROSER 4")
        for farmer_num in range(60, 65):
            self.add_command(f"{farmer_num} ARROSER 5")

    def distribute_sawer(self):
        self.add_command("26 SEMER PATATE 1")
        self.add_command("27 SEMER PATATE 2")
        self.add_command("28 SEMER PATATE 3")
        self.add_command("29 SEMER PATATE 4")
        self.add_command("30 SEMER PATATE 5")

    def distribute_sawer_2(self):
        self.add_command("65 ARROSER 1")
        self.add_command("66 ARROSER 2")
        self.add_command("67 ARROSER 3")
        self.add_command("68 ARROSER 4")
        self.add_command("69 ARROSER 5")

    def distribute_cook(self):
        self.add_command("31 CUISINER")
        self.add_command("32 CUISINER")
        self.add_command("33 CUISINER")
        self.add_command("34 CUISINER")

    def distribute_cook_2(self):
        self.add_command("70 CUISINER")
        self.add_command("71 CUISINER")
        self.add_command("72 CUISINER")
        self.add_command("73 CUISINER")

    def cook(self):
        for OUVRIER in range(31, 35):
            self.add_command(f"{OUVRIER} CUISINER")

    def cook_2(self):
        for OUVRIER in range(70, 74):
            self.add_command(f"{OUVRIER} CUISINER")

    def saw(self, fields):
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        vegetable_to_seed = vegetables[self.vegetable_index]

        for i, field in enumerate(fields):
            if field["content"] == "NONE":
                self.add_command(f"{26 + i} SEMER {vegetable_to_seed} {i + 1}")

        self.vegetable_index = (self.vegetable_index + 1) % len(vegetables)

    def saw_2(self, fields):
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        vegetable_to_seed = vegetables[self.vegetable_index]

        for i, field in enumerate(fields):
            if field["content"] == "NONE":
                self.add_command(f"{65 + i} SEMER {vegetable_to_seed} {i + 1}")

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

    def water_2(
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
            if farmer_id >= 40 and farmer_id <= 44:
                self.add_command(f"{farmer_id} ARROSER 1")
        if need_water_2 != 0:
            if farmer_id > 44 and farmer_id <= 49:
                self.add_command(f"{farmer_id} ARROSER 2")
        if need_water_3 != 0:
            if farmer_id > 49 and farmer_id <= 54:
                self.add_command(f"{farmer_id} ARROSER 3")
        if need_water_4 != 0:
            if farmer_id > 54 and farmer_id <= 59:
                self.add_command(f"{farmer_id} ARROSER 4")
        if need_water_5 != 0:
            if farmer_id > 59 and farmer_id <= 64:
                self.add_command(f"{farmer_id} ARROSER 5")

    def stocker_field1(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 35
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("35 STOCKER 1 1")
            return True

    def stocker_field1_2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 74
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("74 STOCKER 1 1")
            return True

    def stocker_field2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 36
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("36 STOCKER 2 2")
            return True

    def stocker_field2_2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 75
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("75 STOCKER 2 2")
            return True

    def stocker_field3(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 37
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("37 STOCKER 3 3")
            return True

    def stocker_field3_2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 76
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("76 STOCKER 3 3")
            return True

    def stocker_field4(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 38
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("38 STOCKER 4 4")
            return True

    def stocker_field4_2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 77
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("77 STOCKER 4 4")
            return True

    def stocker_field5(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 39
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("39 STOCKER 5 5")
            return True

    def stocker_field5_2(self, content, need_water, farmer_id, farmer_pos, stock_done):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 78
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("78 STOCKER 5 5")
            return True

    def fire(self):
        for OUVRIER in range(1, 40):
            self.add_command(f"0 LICENCIER {OUVRIER}")

    def end_game(self):
        for OUVRIER in range(79, 85):
            self.add_command(f"{OUVRIER} CUISINER")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

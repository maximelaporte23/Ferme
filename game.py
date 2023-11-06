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

    def distribute_sawer(self):
        self.add_command("26 SEMER PATATE 1")
        self.add_command("27 SEMER PATATE 2")
        self.add_command("28 SEMER PATATE 3")
        self.add_command("29 SEMER PATATE 4")
        self.add_command("30 SEMER PATATE 5")
              
    def distribute_cook(self):
        self.add_command("31 CUISINER")
        self.add_command("32 CUISINER")
        self.add_command("33 CUISINER")

    def cook(self):
        for OUVRIER in range(31, 34):
            self.add_command(f"{OUVRIER} CUISINER")

    def saw(self, fields):
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        vegetable_to_seed = vegetables[self.vegetable_index]

        for i, field in enumerate(fields):
            if field["content"] == "NONE":
                self.add_command(f"{26 + i} SEMER {vegetable_to_seed} {i + 1}")

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

    def stocker_field1(
        self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 5
            and content != "NONE"
            and farmer_id == 34
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("34 STOCKER 1 1")
            return True

    def stocker_field2(
        self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 5
            and content != "NONE"
            and farmer_id == 35
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("35 STOCKER 2 2")
            return True

    def stocker_field3(
        self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 36
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("36 STOCKER 3 3")
            return True

    def stocker_field4(
        self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 37
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("37 STOCKER 4 4")
            return True
         
    def stocker_field5(
        self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 38
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command("38 STOCKER 5 5")
            return True
    
    #def fire(self):
    #    for OUVRIER in range(1, 39):
    #        self.add_command(f"0 LICENCIER {OUVRIER}")

    def end_game(self):
        self.add_command("39 CUISINER")
        self.add_command("40 CUISINER")
        self.add_command("41 CUISINER")
        self.add_command("42 CUISINER")
        self.add_command("43 CUISINER")
        self.add_command("44 CUISINER")
        self.add_command("45 CUISINER")
        self.add_command("46 CUISINER")
        self.add_command("47 CUISINER")
        self.add_command("48 CUISINER")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

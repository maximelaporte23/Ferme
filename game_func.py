class Game:
    def __init__(self: "Game") -> None:
        self.commands = []
        self.farmer = []
        self.fields = []

    def hire_farmers(self, nb_farmers):
        for _ in range(nb_farmers):
            self.add_command("0 EMPLOYER")

    def hire_sawer(self, nb_sawers):
        for _ in range(nb_sawers):
            self.add_command("0 EMPLOYER")

    def distribute_sawer(self):
        self.add_command("35 SEMER PATATE 1")
        self.add_command("36 SEMER PATATE 2")
        self.add_command("37 SEMER PATATE 2")
        self.add_command("38 SEMER PATATE 4")
        self.add_command("39 SEMER PATATE 5")

    def distribute_farmers(self, nb_employees, nb_of_chef, nb_of_stocker):
        farmer_num = 0
        for field_num in range(1, 6):
            for _ in range(5):
                farmer_num += 1
                self.add_command(f"{farmer_num} SEMER PATATE {field_num}")
                if farmer_num >= nb_employees - nb_of_chef - nb_of_stocker:
                    return

    def saw(self, fields, stock):
        min_veggie = min(stock, key=stock.get)
        min_veggie_fr = ""
        if min_veggie == "POTATO":
            min_veggie_fr = "PATATE"
        elif min_veggie == "LEEK":
            min_veggie_fr = "POIREAU"
        elif min_veggie == "TOMATO":
            min_veggie_fr = "TOMATE"
        elif min_veggie == "ONION":
            min_veggie_fr = "OIGNON"
        elif min_veggie == "ZUCCHINI":
            min_veggie_fr = "COURGETTE"

        field1 = fields[0]
        field2 = fields[1]
        field3 = fields[2]
        field4 = fields[3]
        field5 = fields[4]
        if field1["content"] == "NONE":
            self.add_command(f"35 SEMER {min_veggie_fr} 1")
        if field2["content"] == "NONE":
            self.add_command(f"36 SEMER {min_veggie_fr} 2")
        if field3["content"] == "NONE":
            self.add_command(f"37 SEMER {min_veggie_fr} 3")
        if field4["content"] == "NONE":
            self.add_command(f"38 SEMER {min_veggie_fr} 4")
        if field5["content"] == "NONE":
            self.add_command(f"39 SEMER {min_veggie_fr} 5")

    def cook(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            self.add_command("30 CUISINER")
            self.add_command("31 CUISINER")
            self.add_command("32 CUISINER")
            self.add_command("33 CUISINER")
            self.add_command("34 CUISINER")
            self.add_command("40 CUISINER")
            self.add_command("41 CUISINER")
            self.add_command("42 CUISINER")
            self.add_command("43 CUISINER")
            self.add_command("44 CUISINER")
            self.add_command("45 CUISINER")

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
            need_water == 0
            and content != "NONE"
            and farmer_id == 26
            and farmer_pos == "SOUP_FACTORY"
            # and not stock_done
        ):
            self.add_command("26 STOCKER 1 1")
            return True

    def stocker_field2(
            self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 27
            and farmer_pos == "SOUP_FACTORY"
            and not stock_done
        ):
            self.add_command("27 STOCKER 2 2")
            return True

    def stocker_field3(
            self, content, need_water, farmer_id, farmer_pos, stock_done
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 28
            and farmer_pos == "SOUP_FACTORY"
            and not stock_done
        ):
            self.add_command("28 STOCKER 3 3")
            return True

    def stocker_field4_5(
        self, content, need_water, farmer_id, farmer_pos, stock_done, nb_field
    ):
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == 29
            and farmer_pos == "SOUP_FACTORY"
            and not stock_done
        ):
            if nb_field == 4:
                self.add_command("29 STOCKER 4 4")
            if nb_field == 5:
                self.add_command("29 STOCKER 5 4")
            return True

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)
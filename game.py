from field import Field
from location import Location
from vegetable import Vegetable
from itertools import chain


class Game:
    def __init__(self: "Game") -> None:
        self.commands = []
        self.farmer = []
        self.fields: list[Field] = [Field(Location.FIELD1), Field(Location.FIELD2), Field(Location.FIELD3), Field(Location.FIELD4), Field(Location.FIELD5)]
        self.vegetable_index = 0
        self.team = 0

    def update_fields(self, fields_json):
        for index, field_json in enumerate(fields_json):
            field = self.fields[index]
            field.needed_water = field_json["needed_water"]
            field.bought = field_json["bought"]
            field.content = Vegetable[field_json["content"]]

    def nbt(self, number):
        return 39 * self.team + number

    def distribute_farmers(self):
        for farmer_num in range(1, 6):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 1")
        for farmer_num in range(6, 11):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 2")
        for farmer_num in range(11, 16):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 3")
        for farmer_num in range(16, 21):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 4")
        for farmer_num in range(21, 26):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 5")

    def distribute_sawer(self):
        self.add_command("26 SEMER PATATE 1")
        self.add_command("27 SEMER PATATE 2")
        self.add_command("28 SEMER PATATE 3")
        self.add_command("29 SEMER PATATE 4")
        self.add_command("30 SEMER PATATE 5")
        #for field in range(1, 6):
        #    for farmer_num in range(26, 31):
        #        self.add_command(f"{self.nbt(farmer_num)} SEMER PATATE {field}")

    def distribute_sawer_2(self):
        self.add_command("65 SEMER PATATE 1")
        self.add_command("66 SEMER PATATE 2")
        self.add_command("67 ARROSER 3")
        self.add_command("68 ARROSER 4")
        self.add_command("69 ARROSER 5")

    def distribute_cook(self):
        for farmer_num in range(31, 35):
            self.add_command(f"{self.nbt(farmer_num)} CUISINER")
    
    def distribute_cook_2(self):
        self.add_command("70 CUISINER")
        self.add_command("71 CUISINER")
        self.add_command("72 CUISINER")
        self.add_command("73 CUISINER")

    def cook(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            for farmer_num in range(31, 35):
                self.add_command(f"{self.nbt(farmer_num)} CUISINER")

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
            self.add_command(f"{self.nbt(26)} SEMER {min_veggie_fr} 1")
        if field2["content"] == "NONE":
            self.add_command(f"{self.nbt(27)} SEMER {min_veggie_fr} 2")
        if field3["content"] == "NONE":
            self.add_command(f"{self.nbt(28)} SEMER {min_veggie_fr} 3")
        if field4["content"] == "NONE":
            self.add_command(f"{self.nbt(29)} SEMER {min_veggie_fr} 4")
        if field5["content"] == "NONE":
            self.add_command(f"{self.nbt(30)} SEMER {min_veggie_fr} 5")

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
            if self.nbt(0) < farmer_id <= self.nbt(5):
                self.add_command(f"{farmer_id} ARROSER 1")
        if need_water_2 != 0:
            if self.nbt(5) < farmer_id <= self.nbt(10):
                self.add_command(f"{farmer_id} ARROSER 2")
        if need_water_3 != 0:
            if self.nbt(10) < farmer_id <= self.nbt(15):
                self.add_command(f"{farmer_id} ARROSER 3")
        if need_water_4 != 0:
            if self.nbt(15) < farmer_id <= self.nbt(20):
                self.add_command(f"{farmer_id} ARROSER 4")
        if need_water_5 != 0:
            if self.nbt(20) < farmer_id <= self.nbt(25):
                self.add_command(f"{farmer_id} ARROSER 5")

    def stocker_field1(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and farmer_id == 38:
            if need_water == 0 and (farmer_pos == "FARM" or farmer_pos == "FIELD1"):
                self.add_command(f"{farmer_id} STOCKER 1 1")
                return True
            if need_water > 5 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 1")
                return True
        return False

    def stocker_field2(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and farmer_id == 39:
            if need_water == 0 and (farmer_pos == "FARM" or farmer_pos == "FIELD2"):
                self.add_command(f"{farmer_id} STOCKER 2 2")
                return True
            if need_water > 5 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 2")
                return True
        return False

    def stocker_field3_4_5(self, field_pos, content, need_water, farmer_id, farmer_pos):
        field_index = int(field_pos[-1])
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == self.nbt(32) + field_index
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command(f"{farmer_id} STOCKER {field_index} {field_index}")
            return True
        return False

    def fire_other(self):
        for farmer_id in chain(range(1, 26), range(31, 35)):
            self.add_command(f"0 LICENCIER {self.nbt(farmer_id)}")

    def fire_stocker_sawer(self):
        for farmer_id in chain(range(26, 31), range(35, 38)):
            self.add_command(f"0 LICENCIER {self.nbt(farmer_id)}")

    def end_game(self):
        for farmer_id in range(77, 80):
            self.add_command(f"{farmer_id} CUISINER")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

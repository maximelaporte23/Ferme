from field import Field
from location import Location
from vegetable import Vegetable


class Game:
    def __init__(self: "Game") -> None:
        self.commands: list[str] = []
        self.farmer: list[str] = []
        self.fields: list[Field] = [
            Field(Location.FIELD1),
            Field(Location.FIELD2),
            Field(Location.FIELD3),
            Field(Location.FIELD4),
            Field(Location.FIELD5)
        ]
        self.vegetable_index = 0
        self.team = 0

    def update_fields(self, fields_json):
        for index, field_json in enumerate(fields_json):
            field = self.fields[index]
            field.needed_water = field_json["needed_water"]
            field.bought = field_json["bought"]
            field.content = Vegetable[field_json["content"]]

    def nbt(self, number):
        return 37 * self.team + number

    def distribute_farmers(self):
        for farmer_num in range(3, 8):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 1")
        for farmer_num in range(8, 13):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 2")
        for farmer_num in range(13, 18):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 3")
        for farmer_num in range(18, 23):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 4")
        for farmer_num in range(23, 28):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 5")

    def distribute_sawer(self, fields):
        for i, field in enumerate(fields):
            self.add_command(f"{self.nbt(28) + i} SEMER PATATE {i + 1}")

    def distribute_sawer_2(self, fields):
        for i, field in enumerate(fields):
            self.add_command(f"{self.nbt(28) + i} ARROSER {i + 1}")

    def distribute_cook(self):
        for farmer_num in range(33, 37):
            self.add_command(f"{self.nbt(farmer_num)} CUISINER")

    def cook(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            for farmer_num in range(33, 37):
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

        for i, field in enumerate(fields):
            if field["content"] == "NONE":
                self.add_command(f"{self.nbt(28) + i} SEMER {min_veggie_fr} {i + 1}")

    def water(
        self,
        need_water_1,
        need_water_2,
        need_water_3,
        need_water_4,
        need_water_5,
        farmer_id,
    ):
        if need_water_1 != 0:
            if self.nbt(2) < farmer_id <= self.nbt(7):
                self.add_command(f"{farmer_id} ARROSER 1")
        if need_water_2 != 0:
            if self.nbt(7) < farmer_id <= self.nbt(12):
                self.add_command(f"{farmer_id} ARROSER 2")
        if need_water_3 != 0:
            if self.nbt(12) < farmer_id <= self.nbt(17):
                self.add_command(f"{farmer_id} ARROSER 3")
        if need_water_4 != 0:
            if self.nbt(17) < farmer_id <= self.nbt(22):
                self.add_command(f"{farmer_id} ARROSER 4")
        if need_water_5 != 0:
            if self.nbt(22) < farmer_id <= self.nbt(27):
                self.add_command(f"{farmer_id} ARROSER 5")

    def stocker_field1(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and farmer_id == 1:
            if need_water == 0 and (farmer_pos == "FARM" or farmer_pos == "FIELD1"):
                self.add_command(f"{farmer_id} STOCKER 1 1")
                return True
            if need_water >= 4 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 1")
                return True
        return False

    def stocker_field2(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and farmer_id == 2:
            if need_water == 0 and (farmer_pos == "FARM" or farmer_pos == "FIELD2"):
                self.add_command(f"{farmer_id} STOCKER 2 2")
                return True
            if need_water >= 4 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 2")
                return True
        return False

    def stocker_field3_4_5(self, field_pos, content, need_water, farmer_id, farmer_pos):
        field_index = int(field_pos[-1])
        if (
            need_water == 0
            and content != "NONE"
            and farmer_id == self.nbt(34) + field_index
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command(f"{farmer_id} STOCKER {field_index} {field_index}")
            return True
        return False

    def fire(self):
        for farmer_id in range(3, 40):
            self.add_command(f"0 LICENCIER {self.nbt(farmer_id)}")

    def end_game(self):
        for farmer_id in range(40, 44):
            self.add_command(f"{self.nbt(farmer_id)} CUISINER")

    def cook_end(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            for farmer_id in range(40, 44):
                self.add_command(f"{self.nbt(farmer_id)} CUISINER")

    def sell(self, need_water):
        if need_water == 0:
            self.add_command("0 VENDRE 1")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

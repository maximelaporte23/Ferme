from notre_ferme.field import Field
from notre_ferme.location import Location
from notre_ferme.vegetable import Vegetable


class Game:
    def __init__(self: "Game") -> None:
        self.commands: list[str] = []
        self.farmer: list[str] = []
        self.fields: list[Field] = [
            Field(Location.FIELD1),
            Field(Location.FIELD2),
            Field(Location.FIELD3),
            Field(Location.FIELD4),
            Field(Location.FIELD5),
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
        return 36 * self.team + number

    def distribute_farmers(self):
        for farmer_num in range(3, 13):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 1")
        for farmer_num in range(14, 24):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 3")
        for farmer_num in range(25, 35):
            self.add_command(f"{self.nbt(farmer_num)} ARROSER 5")

    def distribute_sawer(self, fields):
        self.add_command("13 SEMER PATATE 1")
        self.add_command("24 SEMER PATATE 1")
        self.add_command("35 SEMER PATATE 1")

    def distribute_sawer_2(self, fields):
        self.add_command(f"{self.nbt(13)} ARROSER 1")
        self.add_command(f"{self.nbt(24)} ARROSER 1")
        self.add_command(f"{self.nbt(35)} ARROSER 1")

    def saw(self, fields, stock, farmer_pos):
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
        
        for field in enumerate(fields):
            if field["content"] == "NONE":
                if farmer_pos == "FIELD1":
                    self.add_command(f"{self.nbt(13)} SEMER {min_veggie_fr} 2")
                if farmer_pos == "FIELD2":
                    self.add_command(f"{self.nbt(13)} SEMER {min_veggie_fr} 1")
                if farmer_pos == "FIELD3":
                    self.add_command(f"{self.nbt(24)} SEMER {min_veggie_fr} 4")
                if farmer_pos == "FIELD4":
                    self.add_command(f"{self.nbt(24)} SEMER {min_veggie_fr} 3")
                if farmer_pos == "FIELD5":
                    if (
                        stock["POTATO"] != 0
                        and stock["LEEK"] != 0
                        and stock["TOMATO"] != 0
                        and stock["ONION"] != 0
                        and stock["ZUCCHINI"] != 0
                    ):
                        self.add_command(f"{self.nbt(24)} CUISINER")
                if farmer_pos == "SOUP_FACTORY":
                    self.add_command(f"{self.nbt(35)} SEMER {min_veggie_fr} 5")

    def field1_2(self, content, farmer_pos, farmer_id):
        if content != "NONE" and self.nbt(2) < farmer_id <= self.nbt(12):
            if farmer_pos == "FIELD1":
                self.add_command(f"{farmer_id} ARROSER 2")
            if farmer_pos == "FIELD2":
                self.add_command(f"{farmer_id} ARROSER 1")

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

    def stocker_field3_4_5(
        self, field_pos, content, need_water, farmer_id, farmer_pos, stock
    ):
        field_index = int(field_pos[-1])
        if content != "NONE" and farmer_id == self.nbt(33) + field_index:
            if need_water == 0 and (
                farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM"
            ):
                self.add_command(f"{farmer_id} STOCKER {field_index} {field_index}")
                return True
            if need_water != 0 and farmer_pos == "SOUP_FACTORY":
                if (
                    stock["POTATO"] != 0
                    and stock["LEEK"] != 0
                    and stock["TOMATO"] != 0
                    and stock["ONION"] != 0
                    and stock["ZUCCHINI"] != 0
                ):
                    self.add_command(f"{farmer_id} CUISINER")
                return True
        return False

    def fire(self):
        for farmer_id in range(3, 39):
            self.add_command(f"0 LICENCIER {self.nbt(farmer_id)}")

    def end_game(self):
        for farmer_id in range(39, 43):
            self.add_command(f"{self.nbt(farmer_id)} CUISINER")

    def cook_end(self, stock):
        if (
            stock["POTATO"] != 0
            and stock["LEEK"] != 0
            and stock["TOMATO"] != 0
            and stock["ONION"] != 0
            and stock["ZUCCHINI"] != 0
        ):
            for farmer_id in range(39, 43):
                self.add_command(f"{self.nbt(farmer_id)} CUISINER")

    def sell(self, need_water):
        if need_water == 0:
            self.add_command("0 VENDRE 1")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

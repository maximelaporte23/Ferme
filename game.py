from field import Field
from location import Location
from vegetable import Vegetable


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
        #for field in fields:
        #    for farmer_num in range(26, 31):
        #        self.add_command(f"{farmer_num} SEMER PATATE {field}")

    def distribute_sawer_2(self):
        self.add_command("65 ARROSER 1")
        self.add_command("66 ARROSER 2")
        self.add_command("67 ARROSER 3")
        self.add_command("68 ARROSER 4")
        self.add_command("69 ARROSER 5")
        #for field in fields:
        #    for farmer_num in range(65, 70):
        #        self.add_command(f"{farmer_num} ARROSER {field}")

    def distribute_cook(self):
        self.add_command("31 CUISINER")
        self.add_command("32 CUISINER")
        self.add_command("33 CUISINER")
        self.add_command("34 CUISINER")
        #for farmer_num in range(31, 35):
        #    self.add_command(f"{self.nbt(farmer_num)} CUISINER")
    
    def distribute_cook_2(self):
        self.add_command("70 CUISINER")
        self.add_command("71 CUISINER")
        self.add_command("72 CUISINER")
        self.add_command("73 CUISINER")

    def cook(self):
        for farmer_num in range(31, 35):
            self.add_command(f"{self.nbt(farmer_num)} CUISINER")

    def saw(self, fields):
        farmer_num = 26
        vegetables = ["PATATE", "TOMATE", "OIGNON", "COURGETTE", "POIREAU"]
        vegetable_to_seed = vegetables[self.vegetable_index]

        for i, field in enumerate(fields):
            if field["content"] == "NONE":
                self.add_command(f"{self.nbt(farmer_num) + i} SEMER {vegetable_to_seed} {i + 1}")

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
            if farmer_id <= 5 or 40 < farmer_id <= 44:
                self.add_command(f"{farmer_id} ARROSER 1")
        if need_water_2 != 0:
            if 5 < farmer_id <= 10 or 44 < farmer_id <= 49:
                self.add_command(f"{farmer_id} ARROSER 2")
        if need_water_3 != 0:
            if 10 < farmer_id <= 15 or 49 < farmer_id <= 54:
                self.add_command(f"{farmer_id} ARROSER 3")
        if need_water_4 != 0:
            if 15 < farmer_id <= 20 or 54 < farmer_id <= 59:
                self.add_command(f"{farmer_id} ARROSER 4")
        if need_water_5 != 0:
            if 20 < farmer_id <= 25 or 59 < farmer_id <= 64:
                self.add_command(f"{farmer_id} ARROSER 5")

    def stocker_field1(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and (farmer_id == 35 or farmer_id == 74):
            if need_water == 0 and farmer_pos in ("FIELD3", "FARM"):
                self.add_command(f"{farmer_id} STOCKER 1 1")
                return True
            if need_water == 5 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 3")
                return True
        return False

    def stocker_field2(self, content, need_water, farmer_id, farmer_pos):
        if content != "NONE" and (farmer_id == 36 or farmer_id == 75):
            if need_water == 0 and farmer_pos in ("FIELD3", "FARM"):
                self.add_command(f"{farmer_id} STOCKER 2 2")
                return True
            if need_water == 5 and farmer_pos == "SOUP_FACTORY":
                self.add_command(f"{farmer_id} ARROSER 3")
                return True
        return False

    def stocker_field3_4_5(self, field_pos, content, need_water, farmer_id, farmer_pos):
        field_index = int(field_pos[-1])
        if (
            need_water == 0
            and content != "NONE"
            and (farmer_id == 34 + field_index or farmer_id == 73 + field_index)
            and (farmer_pos == "SOUP_FACTORY" or farmer_pos == "FARM")
        ):
            self.add_command(f"{farmer_id} STOCKER {field_index} {field_index}")
            return True
        return False

    def fire(self):
        for OUVRIER in range(1, 40):
            self.add_command(f"0 LICENCIER {OUVRIER}")

    def end_game(self):
        for OUVRIER in range(79, 82):
            self.add_command(f"{OUVRIER} CUISINER")

    def add_command(self: "Game", command: str) -> None:
        self.commands.append(command)

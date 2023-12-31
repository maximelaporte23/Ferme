from notre_ferme.vegetable import Vegetable
from notre_ferme.location import Location


class Field:
    def __init__(self: "Field", location: Location) -> None:
        self.content: Vegetable = Vegetable.NONE
        self.needed_water = 0
        self.bought = False
        self.location = location

    def __repr__(self: "Field") -> str:
        return (
            f"Field({self.content.name}, needed_water={self.needed_water}, "
            f"bought={self.bought}, location={self.location.name})"
        )

    def is_sowable(self):
        return self.content == Vegetable.NONE and self.bought

    def is_sown(self):
        return self.content != Vegetable.NONE

    def is_watered(self):
        return self.needed_water == 0 and self.is_sown()

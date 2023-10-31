from vegetable import Vegetable
from location import Location


class Field:
    def __init__(self: "Field", location: Location) -> None:
        self.content = Vegetable.NONE
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

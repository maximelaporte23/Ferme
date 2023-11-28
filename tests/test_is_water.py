from notre_ferme.location import Location
from notre_ferme.field import Field
from notre_ferme.vegetable import Vegetable


def test_is_water_without_enough_water():
    field = Field(Location.FIELD1)

    assert not field.is_watered(), "La champ ne devrait pas avoir assez d'eau"


def test_is_water_with_enough_water():
    field = Field(Location.FIELD1)
    field.content = Vegetable.POTATO
    field.needed_water = 0

    assert field.is_watered()

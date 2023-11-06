from location import Location
from field import Field
from vegetable import Vegetable


def test_is_water_without_enough_water():
    field = Field(Location.FIELD1)

    assert not field.is_watered(), "La champ ne devrait pas avoir assez d'eau"


def test_is_water_with_enough_water():
    field = Field(Location.FIELD1)
    field.content = Vegetable.POTATO
    field.needed_water = 0

    assert field.is_watered()


# def test_is_water_without_enough_water():
#     farm_without_enough_water = Field(Location.FIELD2, 5)
#     assert (
#         not farm_without_enough_water.is_water()
#     ), "La champ ne devrait pas avoir assez d'eau"

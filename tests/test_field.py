from vegetable import Vegetable
from field import Field
from location import fields


def test_field_initialization():
    for location in fields:
        field = Field(location)
        assert field.content == Vegetable.NONE
        assert field.needed_water == 0
        assert field.bought is False
        assert field.location == location


def test_field_repr():
    for location in fields:
        field = Field(location)
        field.content = Vegetable.POTATO
        field.needed_water = 5
        field.bought = False

        expected_repr = (
            f"Field(POTATO, needed_water=5, bought=False, location={location.name})"
        )

        assert repr(field) == expected_repr

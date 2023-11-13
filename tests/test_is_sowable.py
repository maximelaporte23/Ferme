from notre_ferme.field import Field
from notre_ferme.location import fields
from notre_ferme.vegetable import Vegetable


def test_is_sowable():
    for location in fields:
        empty_field = Field(location)
        assert empty_field.is_sowable() is False


def test_is_sowable2():
    for location in fields:
        empty_field = Field(location)
        empty_field.bought = True
        assert empty_field.is_sowable() is True


def test_is_sowable3():
    for location in fields:
        field = Field(location)
        field.bought = False
        field.content = Vegetable.POTATO
        assert field.is_sowable() is False


def test_is_sowable4():
    for location in fields:
        field = Field(location)
        field.bought = True
        field.content = Vegetable.POTATO
        assert field.is_sowable() is False

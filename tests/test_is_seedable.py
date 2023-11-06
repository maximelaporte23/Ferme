from field import Field
from vegetable import Vegetable
from location import Location


def test_is_seedable_with_valid_input():
    field = Field(Location.FIELD1)
    assert not field.is_sown(), "Le champ ne devrait pas être semé"


def test_is_seedable_with_planted_content():
    field = Field(Location.FIELD1)
    field.content = Vegetable.POTATO
    assert field.is_sown(), "Le champ devrait être semé"

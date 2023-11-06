from fire import Farmer, nb_farmers_on_field, farmers_state_field


def test_farmers_in_field_1():
    farmer = Farmer(2, 1)
    assert farmer.id == 2
    assert farmer.location == 1


def test_nb_farmers_field():
    farmers = [Farmer(1, 1)]
    assert nb_farmers_on_field(farmers, 1) == 1


def test_nb_farmers_field_two():
    farmers = [Farmer(1, 1), Farmer(2, 1)]
    assert nb_farmers_on_field(farmers, 1) == 2


def farmers_state():
    farmers = [Farmer(2, 3)]
    # assert farmer.id == 2
    # assert farmer.state == 3
    assert farmers_state_field(farmers, 3) == 1
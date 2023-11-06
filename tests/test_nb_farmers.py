from nb_farmers import Farmer, nb_farmers_on_field


def test_farmers_in_field_1():
    farmer = Farmer(2, 1)
    assert farmer.id == 2
    assert farmer.field == 1    
    # assert farmer.free == True


def test_nb_farmers_field():
    farmers = [Farmer(1, 1)]
    assert nb_farmers_on_field(farmers, 1) == 1


def test_nb_farmers_field_two():
    farmers = [Farmer(1, 1), Farmer(2, 1)]
    assert nb_farmers_on_field(farmers, 1) == 2

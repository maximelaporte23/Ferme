from nb_farmers import Farmer, nb_farmers_on_field


def test_farmers_in_field_1():
    farmer = Farmer(2, 1)
    assert farmer.id == 2
    assert farmer.field == 1    
    # assert farmer.free == True


def test_nb_farmers_field_1():
    farmers = [Farmer(1, 1), Farmer(2, 1), Farmer(3, 1), Farmer(4, 1), Farmer(5, 1), Farmer(6, 1)]
    assert nb_farmers_on_field(farmers, 1) == 6 or 7


def test_nb_farmers_field_2():
    farmers = [Farmer(1, 2), Farmer(2, 2), Farmer(3, 2), Farmer(4, 2), Farmer(5, 2), Farmer(6, 2)]
    assert nb_farmers_on_field(farmers, 2) == 6 or 7


def test_nb_farmers_field_3():
    farmers = [Farmer(1, 3), Farmer(2, 3), Farmer(3, 3), Farmer(4, 3), Farmer(5, 3), Farmer(6, 3)]
    assert nb_farmers_on_field(farmers, 3) == 6 or 7


def test_nb_farmers_field_4():
    farmers = [Farmer(1, 4), Farmer(2, 4), Farmer(3, 4), Farmer(4, 4), Farmer(5, 4), Farmer(6, 4)]
    assert nb_farmers_on_field(farmers, 4) == 6 or 7


def test_nb_farmers_field_5():
    farmers = [Farmer(1, 5), Farmer(2, 5), Farmer(3, 5), Farmer(4, 5), Farmer(5, 5), Farmer(6, 5)]
    assert nb_farmers_on_field(farmers, 5) == 6 or 7


def test_new_farmer_is_free():
    farmer = Farmer(1, 2)
    assert farmer.free == True
    


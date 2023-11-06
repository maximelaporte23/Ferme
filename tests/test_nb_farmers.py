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


def test_new_farmer_is_free():
    farmer = Farmer(1, 2)
    assert farmer.free == True
    

def test_farmer_sow_not_free():
    farmer = Farmer(1, 3)
    field = 2
    vegetable = ("TOMATE")
    farmer.sow(field, vegetable)
    assert farmer.free == False   


def test_farmer_sow_not_free_then_free():
    farmer = Farmer(1, 3)
    field = 2
    vegetable = ("TOMATE")
    farmer.sow(field, vegetable)
    #todo: faire passer 10jours 
    assert farmer.free == False


#todo: si récolte 
#todo: si arrose
#todo: si cuisine
#todo: si sotcke

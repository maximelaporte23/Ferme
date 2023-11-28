from notre_ferme.employee import Employee


def test_set_farmer_id():
    farmer_id = 42
    new_farmer_id = 24
    farmer_pos = "FARM"
    employee = Employee(farmer_id, farmer_pos)

    employee.set_farmer_id(new_farmer_id)
    assert employee.get_farmer_id() == new_farmer_id
    print("Le test pour set_farmer_id a réussi.")

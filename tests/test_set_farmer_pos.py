from notre_ferme.employee import Employee


def test_set_farmer_pos():
    farmer_id = 42
    farmer_pos = "FARM"
    new_farmer_pos = "FIELD"
    employee = Employee(farmer_id, farmer_pos)

    # Vérification que set_farmer_pos modifie correctement farmer_pos
    employee.set_farmer_pos(new_farmer_pos)
    assert employee.get_farmer_pos() == new_farmer_pos
    print("Le test pour set_farmer_pos a réussi.")

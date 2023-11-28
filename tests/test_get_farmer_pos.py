from notre_ferme.employee import Employee


def test_get_farmer_pos():
    farmer_id = 42
    farmer_pos = "FARM"
    employee = Employee(farmer_id, farmer_pos)

    assert (
        employee.get_farmer_pos() == farmer_pos
    ), f"Error: Expected {farmer_pos}, but got {employee.get_farmer_pos()}"

    print("Le test pour get_farmer_pos a réussi.")

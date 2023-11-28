from notre_ferme.employee import Employee


def test_get_farmer_id():
    farmer_id = 42
    farmer_pos = "FARM"
    employee = Employee(farmer_id, farmer_pos)

    assert (
        employee.get_farmer_id() == farmer_id
    ), f"Error: Expected {farmer_id}, but got {employee.get_farmer_id()}"

    print("Le test pour get_farmer_id a réussi.")

from notre_ferme.employee import Employee


def test_get_farmer_id():
    farmer_id = 42
    farmer_pos = "FARM"
    employee = Employee(farmer_id, farmer_pos)

    # Vérification que get_farmer_id renvoie la bonne valeur
    assert (
        employee.get_farmer_id() == farmer_id
    ), f"Erreur :  devrait renvoyer {farmer_id}, mais a renvoyé {employee.get_farmer_id()}"

    print("Le test pour get_farmer_id a réussi.")

from notre_ferme.employee import Employee


def test_get_farmer_pos():
    farmer_id = 42
    farmer_pos = "FARM"
    employee = Employee(farmer_id, farmer_pos)

    # Vérification que get_farmer_pos renvoie la bonne valeur
    assert (
        employee.get_farmer_pos() == farmer_pos
    ), f"Erreur :devrait renvoyer {farmer_pos}, mais a renvoyé {employee.get_farmer_pos()}"

    print("Le test pour get_farmer_pos a réussi.")

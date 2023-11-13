from notre_ferme.game import Game


def test_distribute_farmers_function():
    instance = Game()
    instance.distribute_farmers()

    expected_commands = [
        "1 ARROSER 1",
        "2 ARROSER 1",
        "3 ARROSER 1",
        "4 ARROSER 1",
        "5 ARROSER 1",
        "6 ARROSER 2",
        "7 ARROSER 2",
        "8 ARROSER 2",
        "9 ARROSER 2",
        "10 ARROSER 2",
        "11 ARROSER 3",
        "12 ARROSER 3",
        "13 ARROSER 3",
        "14 ARROSER 3",
        "15 ARROSER 3",
        "16 ARROSER 4",
        "17 ARROSER 4",
        "18 ARROSER 4",
        "19 ARROSER 4",
        "20 ARROSER 4",
        "21 ARROSER 5",
        "22 ARROSER 5",
        "23 ARROSER 5",
        "24 ARROSER 5",
        "25 ARROSER 5",
    ]

    if instance.commands == expected_commands:
        print("La méthode distribute_farmers a réussi le test.")
    else:
        print("Les commandes ne sont pas correctes.")

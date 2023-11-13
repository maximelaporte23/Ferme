from notre_ferme.game import Game


def test_fire():
    instance = Game()
    instance.fire()
    expected_commands = [

        "0 LICENCIER 1"
        "0 LICENCIER 2"
        "0 LICENCIER 3"
        "0 LICENCIER 3"
        "0 LICENCIER 4"
        "0 LICENCIER 5"
        "0 LICENCIER 6"
        "0 LICENCIER 7"
        "0 LICENCIER 8"
        "0 LICENCIER 9"
        "0 LICENCIER 10"
    ]
    if instance.commands == expected_commands:
        print('méthode fire réussie')
    else:
        print("méthode fire ratée")




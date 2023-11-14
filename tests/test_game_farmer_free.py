from notre_ferme.game import Game


def test_farmer_is_free():
    actions = [
        # {"content": "SEMER"},
        # {"content": "SEMER2"},
        # {"content": "AROSER"},
        # {"content": "need_water_1"},
        # {"content": "need_water_2"},
        # {"content": "need_water_3"},
        # {"content": "need_water_4"},
        # {"content": "need_water_5"},
        # {"content": "AROSER2"},
        {"content": "CUISINER1"},
        # {"content": "CUISINER2"},
    ]

    instance = Game()
    # assert not instance.saw(actions)
    # assert not instance.saw_2(actions)
    # assert not instance.water(actions)
    # assert not instance.water(actions)
    # assert not instance.water_2(actions)
    assert not instance.cook(actions, field)
    # assert not instance.cook_2(actions)

    expected_commands = [
        # "26 SEMER PATATE 1",
        # "65 SEMER2 TOMATE 2",
        # "28 AROSER 1",
        # "44 AROSER 2",
        # "49 AROSER 3",
        # "54 AROSER 4",
        # "59 AROSER 5",
        # "45 AROSER2 4",
        "31 CUISINER",
        # "71 CUISINER2",
    ]

    if instance.commands == expected_commands:
        print("les ouvriers sont disponibles")
    else:
        print("les ouvrier sont occupés")

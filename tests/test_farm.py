def test_farm_employees():
    farm = Farm()
    farm.hire()
    assert len(farm.employees) == 1
def test_farm_employees2():
    farm = Farm()
    farm.hire()
    farm.hire()
    assert len(farm.employees) == 2
def test_farm_employees3():
    farm = Farm()
    farm.hire()
    farm.hire()
    farm.fire()
    assert len(farm.employees) == 1

from chronobio.game.employee import Employee
from chronobio.game.farm import Farm
from chronobio.game.location import Location

def test_employee_initial_state():
    farm = Farm()
    employee = Employee(farm, id_=1)
    assert employee.location == Location.FARM
    assert employee.tractor is None
    assert employee.salary == 1000
    assert employee.action_to_do == ()
    assert employee._stock_vegetable == Vegetable.NONE

def test_employee_move():
    farm = Farm()
    employee = Employee(farm, id_=1)
    employee._move(Location.FARM)
    assert employee.location == Location.FARM
    employee._move(Location.FARM + 1)
    assert employee.location == Location.FARM + 1
    employee._move(Location.SOUP_FACTORY)
    assert employee.location == Location.SOUP_FACTORY

def test_employee_raise_salary():
    farm = Farm()
    employee = Employee(farm, id_=1)
    initial_salary = employee.salary
    employee.raise_salary()
    assert employee.salary > initial_salary
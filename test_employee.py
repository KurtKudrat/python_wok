import unittest
from employee import Employee


class Employee_annual_salary_raise(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee('kurt','kudrat',20000)


    def test_raise_annual_salary_with_defuld(self):
        new_salary = self.new_employee.give_raise()
        self.assertEqual(new_salary,25000)

    def test_raise_annual_salary_with_set_value(self):
        new_salary = self.new_employee.give_raise(4000)
        self.assertEqual(new_salary,24000)

unittest.main
import unittest

from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for 'employee.py'"""

    def setUp(self):
        """Create a test employee."""
        self.employee1 = Employee('Joe', 'Shmoe', 75000)
        self.employee1.give_raise()
        self.employee2 = Employee('James', 'Smirk', 75000)
        self.employee2.give_raise(2)

    def test_give_default_raise(self):
        """Do employees with no raise amount specified work?"""
        self.assertEqual(80000, self.employee1.salary)

    def test_give_custom_raise(self):
        """Do employees with custom raise amounts specified work?"""
        self.assertEqual(75002, self.employee2.salary)

if __name__=='__main__':
    unittest.main()
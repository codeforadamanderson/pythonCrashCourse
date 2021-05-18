class Employee:
    """Creates a employee."""

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, pay_raise=5000):
        self.salary = self.salary + int(pay_raise)

employee = Employee('Joe', 'Shmoe', 20000)
employee.give_raise()
print(employee.salary)
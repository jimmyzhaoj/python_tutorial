class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_stringt(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Tetser", "User", 60000)

emp_str_1 = "John-Doe-7000"
emp_str_2 = "Joe-SMith-30000"
emp_str_3 = "Jane-Foe-7000"
first, last, pay = emp_str_1.split("-")
new_emp_1 = Employee(first, last, pay)
new_emp_2 = Employee.from_stringt(emp_str_2)

print(new_emp_2.email)
print(new_emp_2.pay)

# Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

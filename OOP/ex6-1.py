class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@company.com"

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("Corey", "Schafer")
emp_2 = Employee("Tetser", "User")
emp_3 = Employee("Tom", "Cock")
emp_1.first = "Jim"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
emp_2.fullname = "Mary Ann"
print(emp_2.first)
print(emp_2.email)
print(emp_2.fullname)

del emp_2.fullname

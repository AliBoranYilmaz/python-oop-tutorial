# Python Object Oriented Programming
import datetime

class Employee:

    raiseAmount = 1.04 #CLASS VARIABLE

# Class variables can be reached ONLY through the class or an instance of the class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

# Each method within a class automatically takes the instance (self) as the first argument
    
    def fullName(self):
        return ("{} {}".format(self.first, self.last))

    def applyRaise(self):
        self.pay = int(self.pay * Employee.raiseAmount)
        # self.raiseAmount could be used instead of Employee.raiseAmount but it is different from each other

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount
        # This is a class method and takes the class (cls) as its first argument

    @classmethod
    def from_string(cls, employeeString):
        first, last, pay = employeeString.split("-")
        return cls(first, last, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        
        else:
            return True
        


emp_1 = Employee("John", "Wick", 50000) #INSTANCE VARIABLE
emp_2 = Employee("Test", "User", 60000) #INSTANCE VARIABLE

print(emp_1.email)
print(emp_2.email)

emp_1.fullName()
Employee.fullName(emp_1)

emp_1.raiseAmount = 1.05

print(Employee.raiseAmount)
print(emp_1.raiseAmount)
print(emp_2.raiseAmount)

Employee.setRaiseAmount(1.12) # This is equal to Employee.raiseAmount = 1.12
print(emp_2.raiseAmount)

emp_str_3 = "Jane-Doe-90000"
emp_3 = Employee.from_string(emp_str_3)
print(emp_3.email)

my_date = datetime.date(2016, 7, 17)
print(Employee.isWorkday(my_date))


class Developer(Employee): # INHERITANCE
    # Inheriting from Employee class
    raiseAmount = 1.3

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # We do not repeat the statements in the init method of Employee class thanks to this
        # Employee.__init__(self, first, last, pay) equals to it but this is commonly used in multiple inheritance
        self.prog_lang = prog_lang

dev_1 = Developer("Ali", "Boran", 50000, "Python")
dev_2 = Developer("Mark", "Krantz", 40000, "Java")
print(dev_2.prog_lang)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def print_employees(self):
        for emp in self.employees:
            emp.fullName()

    def __repr__(self):
        return "Manager('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

# repr and str methods change how our objects are printed and displayed

manager_1 = Manager("Sue", "Smith", 90000, [dev_1])
manager_1.add_employee(dev_2)
manager_1.print_employees()
manager_1.remove_employee(dev_1)
manager_1.print_employees()

print(repr(manager_1))
print(str(manager_1))
# These are exactly same
print(manager_1.__repr__())
print(manager_1.__str__())

# PROPERTY DECORATORS
class Cars():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property # This is a getter. we can use methods like they are an attribute with getters
    def email(self):
        return ("{}.{}@company.com".format(self.first, self.last))

    @property
    def fullName(self):
        return ("{} {}".format(self.first, self.last))

    @fullName.setter # This is a setter
    def fullName(self, toBeGivenName):
        first, last = toBeGivenName.split(" ")
        self.first = first
        self.last = last

    @fullName.deleter # This is a deleter
    def fullName(self):
        print("Name deleted!")
        self.first = None
        self.last = None

car_1 = Cars("Nissan", "Micra")

print("\n")

car_1.first = "Toyota"

print(car_1.first)
print(car_1.email) # Not car_1.email() thanks to the getter
print(car_1.fullName) # Not car_1.fullName() thanks to the getter

del car_1.fullName
print(car_1.fullName)

    

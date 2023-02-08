class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary , role):
        self.name = aname
        self.salary= asalary
        self.role=role

    def printdetails(self):
        return f"the name is  {self.name}  salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class programmer(Employee):
    no_of_leaves = 32

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

harry = Employee("harry", 255,"instructor")
rohan = programmer("Karan", 777, "Programmer", ["python", "Cpp"])

print(rohan.printdetails())

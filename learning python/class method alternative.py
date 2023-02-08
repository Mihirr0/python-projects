class Employee:
    no_of_leaves = 8

    def __init__(self,name, salary, role):
        self.naan = name
        self.tankha = salary
        self.kaam = role

    def printdetails(self):
        return f"the name is {self.naan}. salary is {self.tankha} and role is {self.kaam}"

    @classmethod
    def change_leaves(cls,new):
        cls.no_of_leaves=new

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
mih = Employee("mihir",3230000,"player")
ram = Employee("mishir",3230000,"player")
sham = Employee("mr",3230000,"player")
balram = Employee("balr",3230000,"player")
karan = Employee.from_dash("karan-498-student")


print(karan.tankha)
# sham.change_leaves(14)
print(karan)




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

mih = Employee("mihir",3230000,"player")
ram = Employee("mishir",3230000,"player")
sham = Employee("mr",3230000,"player")
balram = Employee("balr",3230000,"player")
# sham.change_leaves(14)

print(mih.printdetails())
print(mih.tankha)
print(sham.no_of_leaves)
print(mih.no_of_leaves)
print(ram.no_of_leaves)


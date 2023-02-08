# # class Student:
# #     """this is my docstring"""
# #     pass
# #
# # harry = Student()
# # larry = Student()
# #
# # harry.name = "micky"
# # harry.roll_no = "32"
# # larry.subjects = ["hindi","physics"]
# #
# # print(harry.name,larry.subjects)
# # print(Student.__doc__)
#
#
#
# class employee:
#     no_of_leaves =10
#     pass
#
# mike = employee()
# krish =employee()
#
#
# mike.name ="mihir"
# mike.salary=439
# mike.role='student'
#
# krish.name ="krish"
# krish.salary=49
# krish.role='student'
#
# print(krish.__dict__)


class employee:
    no_of_leaves =10

    def __init__(self,an,mam,nan):
        self.name=an
        self.roll=mam
        self.dil=nan
    def printdetails(self):
        return f"the name is {self.name} salary is{self.mam} and role is{self.nan}"
mih = employee("mihir",323,"player")

print(mih.roll)
# mih.printdetails()


# mihir sharma i wamt to becpem a spoft wqere wprM pR
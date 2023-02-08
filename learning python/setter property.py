class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname== None or self.lname== None:
            return f"email is not set . please set it using setter"
        return f" {self.fname} .{self.lname}@codewithharry"

    @email.setter
    def email(self,string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hindustani_supporter = Employee("hindustani","supporter")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"
#
print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)

# del hindustani_supporter.email
# print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.perry@codewithharry.com"
print(hindustani_supporter.email)
# aaj toh aids lagg rha h ki pa nhi kya hp bss halat paltu
# li ho rkhi h but i don't know what u feel to
# let us see what  happens and boom she will come i know
# well i m gonna do the same
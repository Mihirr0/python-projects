def func( normal,*wr,**kr):
    print(normal)
    for bnde in wr:
        print(bnde)
    print(" \nlo ji aab kya kre veer agya")
    for veer,kheer in kr.items():
        print(f" {veer} is a {kheer}")


wr=["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
normal="i am a normal argument:"
func(normal,*wr,**kw)
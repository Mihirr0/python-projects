def function1(func):
    def new():
        print("Subscribe now")
        func()
        print("finished")
    return new

@function1
def me():
    print("it is decorator")

me()
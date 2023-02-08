a=int(input("kitni line chahiye btao\n"))
b=bool(int(input("please add 0 for false or 1 for true")))

def star(a,b):
    if b == True:
        c =1
        while c <= a:
            print(c * "*")
            c = c + 1

    else:
        while a > 0:
            print(a * "*")
            a = a - 1

star(a,b)

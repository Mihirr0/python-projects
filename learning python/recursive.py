def iterative(n):
    """

    :param n: saas
    :return: SMIHR
    """
    fac=1
    for i in range(n):
        fac=fac* (i+1)
    return fac

number=int(input("enter the number\n"))
print("factorial using iterative :",iterative(number))

def recursive(n):
    if n==1:
        return 1
    else:
        return n*recursive(n-1)
print("factorial using recursive :",recursive(number))

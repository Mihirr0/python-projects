items =[1,2,3,4,5]
a=list(map((lambda x:x**3),items))
# print(a)

a=[1,2,3,4,5]
b=[2,3,4,65,3]
c=list(filter(lambda x: x in a,b))
print(c)

from functools import reduce

list1 =[1,3,4,5]
num = reduce(lambda  x,y:x*y,list1)
print(num)
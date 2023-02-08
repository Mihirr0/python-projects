# i have taken 32 as my number
guess=1
print("apko  2 baari mei ek number guess krna hai : ")
while(guess<=2):
    n1=int(input())
    if n1<32:
        print('enter thoda bada')
    elif n1>32:
        print('enter thoda chota')
    else:
        print('jeet gaye')
        print(guess,' baari chli aur jeet gye')
        break
    print(2-guess,'baari bacchi hai bss')
    guess=guess+1

if(guess>2):
            print('baari khatam tum haar gye')

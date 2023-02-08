import random
lst=['s','w','g']

chance=10
no_of_chances=0
comp_pont=0
player_point=0

print("\t\t\t\t\t\t snake ,water,gun  game\n")
print("s fo snake\ng for gun\n w for water")

while no_of_chances<chance:
    _input=input("snake,water,gun:")
    _rand=random.choice(lst)

    if _input==_rand:
        print("draw ho gaya dono ko 0 point")

    elif _input=="s" and _rand=="g":
        comp_pont=comp_pont+1
        print(f"your guess {_input} and  the computer guess  {_rand}\n ")
        print("computer got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")

    elif _input=="s" and _rand=="w":
        player_point=player_point+1
        print(f"your guess {_input} and  the computer guess{_rand}\n")
        print("you got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")
    elif _input=="w" and _rand=="g":
        player_point=player_point+1
        print(f"your guess {_input} and  the computer guess{_rand}\n")
        print("you got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")


    elif _input == "w" and _rand == "s":
        comp_pont = comp_pont + 1
        print(f"your guess {_input} and  the computer guess{_rand}\n")
        print("computer got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")
    elif _input == "g" and _rand == "w":
        comp_pont = comp_pont + 1
        print(f"your guess {_input} and  the computer guess{_rand}\n")
        print("computer got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")
    elif _input == "g" and _rand == "s":
        player_point = player_point + 1
        print(f"your guess {_input} and  the computer guess{_rand}\n")
        print("you got 1 point\n")
        print(f"computr point is {comp_pont} and player point is {player_point}")
    else:
        print("you have input wrong \n")

    no_of_chances = no_of_chances + 1
    print(f"{chance - no_of_chances} is left out of {chance} \n")
print("game over")

if comp_pont==player_point:
    print("tie")
elif comp_pont>player_point:
    print("computer win")
elif player_point>comp_pont:




    print('you win')
print(f"your point is {player_point} and computer point is {comp_pont}")
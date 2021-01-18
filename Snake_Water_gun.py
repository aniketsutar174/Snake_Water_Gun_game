import random
lst =['s','w','g']

chance = 5
no_of_chance = 0
com_point = 0
hum_point = 0

print("choice snake(s),water(w),gun(g)\n")
while no_of_chance < chance:

    inp = input('snake, water, gun\n')
    rand = random.choice(lst)
    if inp == rand:
        print("tie\n")
    #input s
    elif inp == "s" and rand == "g":
        com_point = com_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("computer won..")
        print(f"computer point is {com_point} and human point is {hum_point}\n")
    elif inp == "s" and rand == "w":
        hum_point = hum_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("you  won..\n")
        print(f"computer point is {com_point} and human point is {hum_point}\n")

    #input w
    elif inp == "w" and rand == "g":
        com_point = com_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("computer won..\n")
        print(f"computer point is {com_point} and human point is {hum_point}\n")
    elif inp == "w" and rand == "s":
        hum_point = hum_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("you  won..")
        print(f"computer point is {com_point} and human point is {hum_point}\n")

    #input g
    elif inp == "g" and rand == "s":
        com_point = com_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("computer won..\n")
        print(f"computer point is {com_point} and human point is {hum_point}\n")
    elif inp == "g" and rand == "w":
        hum_point = hum_point + 1
        print(f"your guss is {inp} and computer is {rand}\n")
        print("you  won..")
        print(f"computer point is {com_point} and human point is {hum_point}\n")
    else:
        print("Wrong input..!\n")
    no_of_chance = no_of_chance + 1
print("game over\n")

if com_point == hum_point:
    print("Its tie..\n")
elif com_point<hum_point:
    print(f"You won by {hum_point} point\n")
else:
    print("computer loose\n")
print(f"your point {hum_point} and computer point is {com_point}\n")


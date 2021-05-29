from math import inf
import random
min_value = 1
max_value = 6

roll_again = "yes"
while inf(min_value,max_value) :
    if roll_again == "yes":
        print("rolling the dice")
        print("The Value are :")
        print(random.randint(min_value,max_value))
        print(random.randint(min_value,max_value))
    else:
        print("End")
    roll_again = input("Roll the dices again?")


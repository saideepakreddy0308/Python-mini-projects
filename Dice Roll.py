import random

min_val = 1
max_val = 6

roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices(2)..")
    print("The values are: ")
    #Generating 1st random number in 1-6 and printing
    print(random.randint(min_val, max_val))
    #Generating 2st random number in 1-6 and printing
    print(random.randint(min_val, max_val))

    roll_again = input("Roll the dices again?")
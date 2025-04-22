import random
from random import randint

top_range_num=input("Type a number: ")
if top_range_num.isdigit():
    top_range_num=int(top_range_num)
    if top_range_num <=0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please enter a numbers only")
    quit()
random_number=randint(0,top_range_num)
guess=0
while True:
    guess+=1
    user_guess=input("Enter your guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number only")
        continue
    if user_guess == random_number:
        print("You got it")
        break
    else:
        if user_guess > random_number:
            print("You are above the number")
        else:
            print("you are below the number")
print("You got it in ",guess,"guess")
name= input("Type your name: ")
print("Welcome",name, "to this adventure")

answer=input(" you are on a dirt road,it has to come an end and you can go left or right.which way would like to go? ").lower()


if answer =="left":
   answer =input("you come to a river,you can walk around it or swim across ? Type walk to walk and swim to Swim across: ").lower()
   if answer =="swim":
       print( " You swim across and were eaten by alligator. ")
   elif answer =="walk":
       print(" you walked for many miles,ran out of water and you lost the game")
   else:
       print("Not a valid option, you lose.")

elif answer =="right":
    answer=input("you come to a bridge,it looks wobbly,do you want to cross it or head back (cross/back)? ").lower()
    if answer =="cross":
        answer=input("you cross the bridge and meet a stranger.Do you talk them yes/no? ").lower()
        if answer=="yes":
            print("you talk to the stranger and they give you gold. YOU WIN!")

        elif answer=="no":
            print("you ignore the strange they offended and you lose. ")

        else:
            print("Not a valid option")

    elif answer =="back":
        print(" you go back and lose..")

else:
    print("Not a valid option, You Lose. ")

print("Thank you for trying ",name)
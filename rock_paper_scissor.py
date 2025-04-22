import random

user_wins=0;
computer_wins=0;
options=['rock','paper','scissor'];
while True:
    user_input=input('Type a Rock/Paper/Scissor  or Q to quit ').lower();

    if(user_input == 'q'):
      quit();
    if user_input not in options:
        continue;
    random_number=random.randint(0,2);
    computer_pick=options[random_number];
    print("Computer Picked", computer_pick + ".");
    if user_input =='rock' and computer_pick =="scissor":
        print("You win!");
        user_wins+=1;
        continue;
    elif user_input =='paper' and computer_pick =="rock":
        print("You win!");
        user_wins+=1;
        continue;
    elif user_input =='scissor' and computer_pick =="paper":
        print("You win!");
        user_wins+=1;
        continue;
    else:
        print("You lost!");
        computer_wins+=1;
print("You won ",user_wins,"times.");
print("The computer wins" ,computer_wins,"times.");
print("Good Bye!");

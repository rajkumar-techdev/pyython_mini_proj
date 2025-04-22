print('Welcome to my computer quiz')
playing=input('Do you want to play' )
if playing.lower()!='yes':
   quit()
print("Okay lets play :)")
score=0
answer=input('What does cpu stands for')
if answer.lower() == 'central processing unit':
     print('Correct')
     score+=1
else:
     print('Incorrect')
answer=input('What does gpu stands for')
if answer.lower() == 'graphical processing unit':
     print('Correct')
     score += 1
else:
     print('Incorrect')
answer=input('What does ram stands for')
if answer.lower() == 'random access memory':
     print('Correct')
     score += 1
else:
     print('Incorrect')
answer=input('What does rom stands for')
if answer.lower() == 'read only memory':
     print('Correct')
     score += 1
else:
     print('Incorrect')
print("you got"  + str(score)+  "Questions corrects")
print("you got"  + str((score/4) *100) +  '%')
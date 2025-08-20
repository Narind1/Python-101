import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
stp=[rock,paper,scissors]
a=int(input("Enter your choice:\nEnter 0 for rock,1 for paper or 2 for scissors.\n---"))
b=random.randint(0,2)
i=1
if a>2 :
    print("Enter valid input")
else:
    print("Your choice:",stp[a])
    print("Computer choice:",stp[b])
    if a==b:
        print("Its a draw")
    elif ((a==0) and (b==2)) or ((a==1) and (b==0)) or ((a==2) and (b==1)):
        print("You win")
    elif ((a==2) and (b==0)) or ((a==1) and (b==2)) or ((a==0) and (b==1)):
        print("You lose")
    else:
        print("Enter valid input")
#Write your code above this line

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
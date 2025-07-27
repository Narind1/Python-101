#make a game of higher or lower"
from my_art import logo
from my_art import vs
from game_data import data
import random
while(1):
    while(1):
        a=random.choice(data)
        b=random.choice(data)
        if (a!=b):
            break
        else:
            continue
    print(logo)
    c=a.get('name')
    d=b.get('name')
    print(c)
    print(vs)
    print(d)
    e=a.get('follower_count')
    f=b.get('follower_count')
    if (e>f):
        win=e
    else:
        win=f
    choice=input("Enter your choice:1/2")
    if choice==win:
        print("You win")
        print(a,b)
    else:
        print("You lose")
        print(a,b)
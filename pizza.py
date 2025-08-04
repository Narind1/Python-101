print("Thank you for choosing Fast Pizza Delivery \n")
a=input("What type of pizza do you want:\n 1.Small pizza : 150 \n 2.Medium pizza : 200 \n 3.Large pizza : 400\n---" )
if (a.lower()=="small"):
    price=150
    p=input("Do you want to add pepperoni: y/n\n---")
    if p=='y':
        price=price+70
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    else:
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    print("Please collect you pizza \n The total price is:",price)
elif (a.lower()=="medium"):
    price=200
    p=input("Do you want to add pepperoni: y/n\n---")
    if p=='y':
        price=price+100
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    else:
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    print("Please collect you pizza \n The total price is:",price)
elif (a.lower()=="large"):
    price=400
    p=input("Do you want to add pepperoni: y/n\n---")
    if p=='y':
        price=price+150
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    else:
        c=input("Do you want to add cheese:y/n\n---")
        if c=='y':
            price+=50
    print("Please collect you pizza \n The total price is:",price)
else:
    print("Enter the input correctly:")
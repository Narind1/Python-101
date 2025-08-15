try:
    num = int(input("Enter the number:"))
    print(num**2)
except(KeyboardInterrupt):
    print("You should have entered a number .....Program Terminating.....")
except(ValueError):
    print("You should have entered a number .....Program Terminating.....")
print("Bye")
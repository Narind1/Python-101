a=5
b=3
for i in range (1,101):
    if i%a==0:
        print("Fizz")
    elif i%b==0:
        print("Buzz")
    elif (i%b and i%a)==0:
        print("fizzbuzz")
    else:
        print(i)
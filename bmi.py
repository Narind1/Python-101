w=float(input("Enter your weight in kg:"))
h=float(input("Enter you height in metres:"))
bmi=w/(h)**2
g=input("Enter your gender:m/f")
print("your bmi is:",bmi)
if 18.5<=bmi<=24.9:
    print("You are healthy.")
elif bmi<=18.5:
    print("You are underweight.")
elif 25<=bmi<=29.9:
    print("You are overweight")   
elif 30<=bmi<=34.9:
    print("You are obese.")
else:
    print("You are extremely obese.") 
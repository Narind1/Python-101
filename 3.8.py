print("Enter the marks of 5 subjects:")
m1=int(input("1."))
m2=int(input("2."))
m3=int(input("3."))
m4=int(input("4."))
m5=int(input("5."))
per=(m1+m2+m3+m4+m5)/5
print("percentage :",per,"%")
cgpa=per//10
if 9.1<=cgpa<=10:
    grade="O+"
elif 8.1<=cgpa<=9:
    grade="A+"
elif 7.1<=cgpa<=8:
    grade="A"
elif 6.1<=cgpa<=7:
    grade="B+"
elif 5.1<=cgpa<=6:
    grade="B"
elif 3.5<=cgpa<=5:
    grade="C+"
else:
    grade="F"
print("\t\t\tGRADE CARD\n")
print("Name : Narind verma \nRoll Number : R12345678 \t\t SAPID: 500123456\nSem:1\t\t\t\tCourse:B.Tech.CSE AI&ML")
print("Subject name:\t\tMarks\nPDS:\t\t\t",m1,"\nPython:\t\t\t",m2,"\nChemistry:\t\t",m3,"\nEnglish:\t\t",m4,"\nPhysics:\t\t",m5,"\n\n\nPercentage:\t\t",per,"%","\nCGPA:\t\t\t",cgpa,"\nGrade:\t\t\t",grade)
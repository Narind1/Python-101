students = {"Hermione": 99, "Harry": 82, "Ron": 78, "Draw": 72, "Nevil": 62}

grades_and_performance = {}  

for name, grade in students.items():
    if grade > 91:
        performance = "Outstanding"
    elif grade > 81:
        performance = "Very Good"
    elif grade > 71:
        performance = "Acceptable"
    else:
        performance = "Fail"
    grades_and_performance[name] = (grade, performance)
    

print(f"{grades_and_performance})")
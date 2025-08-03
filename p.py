rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(i, 0, -1):
        print(" * ", end="")
    print()
num = int(input("Enter the number of test cases:"))

for i in range(num):
    try:
        a, b = input("Enter two numbers:").split()

        a = int(a)
        b = int(b)

        print(a / b)
    except KeyboardInterrupt:
        print("Error Code: Enter values")

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError:
        print("Error Code: invalid literal for int() with base 10:", b)

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n,end=' ')
n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, ":")
print_numbers(n)

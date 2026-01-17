def fibonacci(n, a=0, b=1, count=0):
    if count < n:
        print(a, end=" ")
        fibonacci(n, b, a + b, count + 1)
n = int(input("Enter the number of terms: "))
print("Fibonacci series up to", n, "terms:")
fibonacci(n)

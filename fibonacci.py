#program in python to print fibonacci series
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number of terms: "))
fib_series = [fibonacci(i) for i in range(n)]
print("Fibonacci series:", fib_series)
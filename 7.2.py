def sum_of_cubes(n):
    sum_cubes = 0
    for i in range(1, n):
        sum_cubes += i ** 3
    return sum_cubes
n = int(input("Enter a positive integer: "))
result = sum_of_cubes(n)
print("Sum of cubes of positive integers smaller than", n, "is:", result)

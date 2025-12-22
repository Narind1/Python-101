'''Given a string containing both upper and lower case alphabets. Write a Python
program to count the number of occurrences of each alphabet (case
insensitive) and display the same.'''
i = input("Enter a string: ")
a = {}
for char in i:
    l = char.lower()
    if l.isalpha():
        a[l] = a.get(l, 0) + 1
for alphabet, count in a.items():
    print(f"{count}{alphabet}")
'''l=i.upper
for char in i:
    if ord(char) in ()'''
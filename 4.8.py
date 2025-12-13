string = input("Enter a string:")
upper_case_string = ""

for char in string:
    if 'a' <= char <= 'z':
        upper_case_string += chr(ord(char) - 32)
    else:
        upper_case_string += char

print(upper_case_string)

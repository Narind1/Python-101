test_tuple = ("apple", "banana", "cherry")
string_with_comma = ", ".join(test_tuple) # Join with comma and space
string_without_separator = "".join(test_tuple) # Join without separator (concatenate)

print(f"String with comma: {string_with_comma}")
print(f"String without separator: {string_without_separator}")
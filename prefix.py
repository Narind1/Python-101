strings = ["flower", "flow", "flight"]
min_str = min(strings, key=len)
for i, char in enumerate(min_str):
    if all(s[i] == char for s in strings):
        continue
    else:
        common_prefix = min_str[:i]
        break
else:
    common_prefix = min_str
print("Common prefix:", common_prefix)
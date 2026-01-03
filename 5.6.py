# Program to count number of unique words in a given sentence using sets.
a=input("ENter a sentence:")
b=a.split()
'''print(b)
print(a)'''
unique_words = []
for word in b:
    if word not in unique_words:
        unique_words.append(word)
    else:
        unique_words.remove(word)
print("Unique words:",len(unique_words))
#or use set function
#Create a dictionary of n persons where key is name and value is city.
#a) Display all names
#b) Display all city names
#c) Display student name and city of all students.
#d) Count number of students in each city.
person_dict = {
    "Alice": "London",
    "Bob": "Paris",
    "Charlie": "New York",
    "David": "Berlin",
    "Eve": "Madrid"
}
print("Type \n a to Display all names\n b to Display all city names\n c to Display student name and city of all students\n d to Count number of students in each city\n")
a=input()
if a=="a":
    for name in person_dict.keys():
        print("Name:",name)
elif a=="b":
    for city in person_dict.values():
        print("Cities",city)
elif a=="c":
    print("Name - City")
    for name, city in person_dict.items():
        print(f"{name} - {city}")
else:
    print("Number of people from each city:")
    city_counts = {}
    for city in person_dict.values():
        if city not in city_counts:
            city_counts[city] = 0
        city_counts[city] += 1

    for city, count in city_counts.items():
        print(f"{city}: {count}")
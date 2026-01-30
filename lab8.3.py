filename = "city.txt"
with open(filename, 'w') as file:
    city = ["Dehradun 5.78 308.20\n", "Delhi 190 1484\n"]
    file.writelines(city)
with open('city.txt', 'r') as file:
        print("Details of all cities:")
        for line in file:
            city, population, area = line.split()
            print(f"City: {city}, Population: {population} Lakhs, Area: {area} sq KM")
        print("\nCities with population more than 10 Lakhs:")
        for line in file:
            city, population, _ = line.split()
            if float(population) > 10:
                print(city)

with open('city.txt', 'r') as file:
        total_area = sum(float(line.split()[2]) for line in file)
        print("\nSum of areas of all cities:", total_area, "sq KM")
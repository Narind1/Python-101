#Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name, year, director name,
# production cost,collection made (earning) & perform the following :-
#a) print all movie details
#b) display name of movies released before 2015
#c) print movies that made a profit.
#d) print movies directed by a particular director.
movies = {}
num_movies = int(input("Enter the number of movies: "))

for i in range(num_movies):
    movie_name = input("Enter movie name: ")
    year = int(input("Enter year of release: "))
    director = input("Enter director's name: ")
    production_cost = float(input("Enter production cost: "))
    collection_made = float(input("Enter collection made (earning): "))
    
    movies[movie_name] = {
        "year": year,
        "director": director,
        "production cost": production_cost,
        "collection made": collection_made
    }
print("\nAll Movie Details:")
for movie, details in movies.items():
    print(f"\nMovie: {movie}")
    for key, value in details.items():
        print(f"\t{key.capitalize()}: {value}")
print("\nMovies released before 2015:")
for movie, details in movies.items():
    if details["year"] < 2015:
        print(movie)
print("\nMovies that made a profit:")
for movie, details in movies.items():
    if details["collection made"] > details["production cost"]:
        print(movie)
director = input("\nEnter a director's name to filter movies: ")
print(f"\nMovies directed by {director}:")
for movie, details in movies.items():
    if details["director"] == director:
        print(movie)
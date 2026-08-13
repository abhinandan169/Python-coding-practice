# Create a Movie class with attributes title and rating (out of 10). Create a list of 5 Movie objects with different ratings. Loop through and print the titles of movies with rating 7 or above.


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

m1 = Movie("KGF", 10)
m2 = Movie("RRR", 6)
m3 = Movie("Salaar", 8)
m4 = Movie("Doremone", 9)
m5 = Movie("Shinchan", 7)

Movies = [m1, m2, m3, m4, m5]

for movie in Movies:
    if movie.rating >= 7:
        print(f"Movie is {movie.title} and is rating {movie.rating}")       
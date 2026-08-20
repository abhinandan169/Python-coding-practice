# Create a Movie class with attributes title and genre. Create a list of 5 Movie objects with different genres (e.g., "Action", "Comedy", "Drama"). Loop through and print only the titles where genre == "Action"


class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

m1 = Movie("KGF", "Action")        
m2 = Movie("Pushpa", "Action")        
m3 = Movie("Hera Pheri", "Comedy")        
m4 = Movie("Taare Zameen par", "Drama")        
m5 = Movie("RRR", "Action")       


movies = [m1, m2, m3, m4, m5]

for movie in movies:
    if movie.genre == "Action":
        print(movie.title)
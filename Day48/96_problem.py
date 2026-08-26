# Create a class Playlist that stores a list of songs. Add methods add_song(name) to add a song, and total_songs() that returns how many songs are in the playlist.

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, name):
        self.songs.append(name)

    def total_songs(self):
        return len(self.songs)

p1 = Playlist()
p1.add_song("Tum Hi Ho")
p1.add_song("Kesariya")
p1.add_song("Apna Bana Le")

print(p1.total_songs())     
# Create a class Song with attributes title and duration (in seconds). Create a class Playlist that stores a list of Song objects. Add a method total_duration() that returns the sum of durations of all songs in the playlist.


class Song():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Playlist():
    def __init__(self):
        self.song_list = []

    def total_duration(self):
        total = 0
        for song in self.song_list:
            total += song.duration
        return total


p = Playlist()
p.song_list.append(Song("Kesariya", 240))
p.song_list.append(Song("Tum Hi Ho", 300))
p.song_list.append(Song("Apna Bana Le", 280))

print(p.total_duration())
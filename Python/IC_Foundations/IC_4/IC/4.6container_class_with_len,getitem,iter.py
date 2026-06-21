class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __iter__(self):
        return iter(self.songs)
    
p = Playlist(["song1", "song2", "song3"])
print(len(p))
print(p[0]) 
print(p[-1])
print("song2" in p)
for song in p:
    print(song)
print(list(reversed(p)))
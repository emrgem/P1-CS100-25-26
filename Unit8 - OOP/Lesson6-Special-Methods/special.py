# =============================================================================
# PARENT CLASS (from Lesson 4 Day 1) — already done, don't change
# ============================================================================
class Playlist:
    """A music playlist with songs."""

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []

    def add_song(self, title, artist, duration):
        song = {"title": title, "artist": artist, "duration": duration}
        self.songs.append(song)

    def remove_song(self, title):
        for song in self.songs:
            if song["title"] == title:
                self.songs.remove(song)
                return True
        return False

    def song_count(self):
        return len(self.songs)

    def total_duration(self):
        total = 0
        for song in self.songs:
            total += song["duration"]
        return total
    
    def __str__(self): #what print() shows
        """User friendly string for print()"""
        return f"Playlist '{self.name}', by {self.owner} - {self.song_count()} songs"
    
    def __repr__(self): # This is what you see in the REPL/DEBUGGER
        """Developer-friendly string for debugging"""
        return f"Playlist(name='{self.name}', owner='{self.owner}', songs={self.songs}"
    
    def __len__(self):
        """Called by len(playlist)"""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Called by playlist[index]"""
        return self.songs[index]

# =============================================================================
# YOUR CHILD CLASS
# =============================================================================
class CollaborativePlaylist(Playlist):   # ← fix this line (TODO 1)

    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.contributors = []
        
    def add_contributor(self, username):
        self.contributors.append(username)

    def add_song(self, title, artist, duration, added_by = "unknown"):
        super().add_song(title, artist, duration) # adds song to the end of the list
        self.songs[-1]["added_by"] = added_by #adds contributor to the last added song
    
    # New Getter - filter songs by contributor
    def get_songs_by(self, username):
        result = []
        for song in self.songs:
            if song.get("added_by") == username:
                result.append(song['title'])
        return result
# =============================================================================
# TESTS —
# =============================================================================

collab = CollaborativePlaylist("Road Trip", "maria")
print(f"Name:    {collab.name}")           # Road Trip
print(f"Owner:   {collab.owner}")          # maria
print(f"Songs:   {collab.songs}")          # []
print(f"Contribs: {collab.contributors}")  # []
print()


collab.add_song("Dreams", "Fleetwood Mac", 257, added_by="Nick")
collab.add_song("Africa", "Toto", 295, added_by= "Angad" )

text = "Hello BT!"
print(type(text))

print(collab)
print(repr(collab))
print(type(collab))
print(len(collab))
print(collab[0])
print(collab[1])





print(text)
print(repr(text))
print(len(text))
print(text[0])
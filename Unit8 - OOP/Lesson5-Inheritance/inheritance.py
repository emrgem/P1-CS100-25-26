"""======================================================
 UNIT 8 - LESSON 5 - DAY 1: Inheritance Basics
 CollaborativePlaylist extends Playlist
========================================================
SYNTAX TO REMEMBER:
  class Child(Parent):                 ← how you inherit
      def __init__(self, ...):
          super().__init__(...)        ← run parent's __init__ first
          self.new_thing = ...         ← add your new stuff
========================================================"""

# =============================================================================
# PARENT CLASS (from Lesson 4 Day 1) — already done, don't change
# =============================================================================

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


# =============================================================================
# YOUR CHILD CLASS
# =============================================================================
#
# TODO 1: Make CollaborativePlaylist inherit from Playlist
#         Hint: class CollaborativePlaylist(Playlist):
#
# TODO 2: In __init__:
#           - Call super().__init__(name, owner)
#           - Add self.contributors = []   (a new empty list)
#
# TODO 3: Write add_contributor(self, username)
#           - Appends username to self.contributors
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
# TESTS — uncomment as you finish
# =============================================================================

collab = CollaborativePlaylist("Road Trip", "maria")
print(f"Name:    {collab.name}")           # Road Trip
print(f"Owner:   {collab.owner}")          # maria
print(f"Songs:   {collab.songs}")          # []
print(f"Contribs: {collab.contributors}")  # []
print()

# # Inherited methods should work for FREE
# collab.add_song("Dreams", "Fleetwood Mac", 257)
# collab.add_song("Africa", "Toto", 295)
print(f"Song Count: {collab.song_count()}")
print(f"Total Duration: {collab.total_duration()}")


# # Your new method
collab.add_contributor("Nick")
collab.add_contributor("Angad")
print(f"Contributors: {collab.contributors}")

# Test MEthod Overriding - add_song()
collab.add_song("Dreams", "Fleetwood Mac", 257, added_by="Nick")
collab.add_song("Africa", "Toto", 295, added_by= "Angad" )

print(collab.songs)
for song in collab.songs:
    print(f"{song['title']} - added by {song['added_by']}")
    
print("get songs by:")
print(f" Nick's Songs: {collab.get_songs_by('Nick')}")
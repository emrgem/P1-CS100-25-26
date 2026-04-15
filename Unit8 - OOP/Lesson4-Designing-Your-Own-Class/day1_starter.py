"""
=============================================================================
 UNIT 8 - LESSON 4 - DAY 1: Designing Your Own Class - Playlist
=============================================================================
REMEMBER:
  - Each song is a dict: {"title": ..., "artist": ..., "duration": ...}
  - Test each method BEFORE writing the next one
=============================================================================
"""

class Playlist:
    """A music playlist with songs."""

    # -------------------------------------------------------------------------
    # STEP 4: __init__
    # Attributes:
    #   self.name   — playlist name (from parameter)
    #   self.owner  — who made it (from parameter)
    #   self.songs  — empty list to start
    # -------------------------------------------------------------------------
    def __init__(self, name, owner):
      self.name = name
      self.owner = owner
      self.songs = []  

    # -------------------------------------------------------------------------
    # STEP 5a: add_song  (modifier)
    # Takes title, artist, duration
    # Builds a dict and appends it to self.songs
    # -------------------------------------------------------------------------
    def add_song(self, title, artist, duration):
      song = {
        "title": title,
        "artist": artist,
        "duration": duration
      }
      self.songs.append(song)


    # -------------------------------------------------------------------------
    # STEP 5b: remove_song  (conditional modifier)
    # Loop through self.songs
    # If a song's title matches, remove it and return True
    # If no match after the loop, return False
    # -------------------------------------------------------------------------
    

    # -------------------------------------------------------------------------
    # STEP 5c: song_count  (getter)
    # Return the number of songs (use len())
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # STEP 5d: total_duration  (getter)
    # Loop through self.songs, sum up the "duration" of each
    # Return the total
    # -------------------------------------------------------------------------


# =============================================================================
# TESTS — write and run as you finish each method
# =============================================================================

if __name__ == "__main__":
  # Test __init__
  road_trip = Playlist("Road Trip Mix", "Maria")
  print(f"Name: {road_trip.name}")
  print(f"Owner: {road_trip.owner}")
  print(f"Songs: {road_trip.songs}")
  print()
  
  # Test add_song
  road_trip.add_song("Dreams", "Fleetwood Mac", 257)
  road_trip.add_song("Mr. Blue Sky", "ELO",  304)
  road_trip.add_song("Africa", "Toto", 295)
  print(f"  After adding 3 Songs:")
  for song in road_trip.songs:
    print(f"  {song}")
  print()
    

  # Test song_count

  # Test total_duration

  # Test remove_song


from task1 import calculate_remaining
from task2 import create_song
from task3 import playlist_stats
from task4 import build_playlist

if __name__ == "__main__":
        print("=" * 60)
        print("🎵 PRACTICE PERFORMANCE TASK - TEST RESULTS")
        print("=" * 60)
    
        total_points = 0
    
        # Task 1 Tests
        print("\n📋 TASK 1: calculate_remaining")
        print("-" * 40)
        task1_points = 0
    
        try:
            result = calculate_remaining(180, 60)
            if result == 120:
                print("  ✅ Test 1.1 PASSED: calculate_remaining(180, 60) = 120")
                task1_points += 5
            else:
                print(f"  ❌ Test 1.1 FAILED: Expected 120, got {result}")
        
            result = calculate_remaining(200, 200)
            if result == 0:
                print("  ✅ Test 1.2 PASSED: calculate_remaining(200, 200) = 0")
                task1_points += 5
            else:
                print(f"  ❌ Test 1.2 FAILED: Expected 0, got {result}")
        
            result = calculate_remaining(150, 200)
            if result == 0:
                print("  ✅ Test 1.3 PASSED: calculate_remaining(150, 200) = 0 (not -50)")
                task1_points += 5
            else:
                print(f"  ❌ Test 1.3 FAILED: Expected 0, got {result}")
        
            result = calculate_remaining(300, 0)
            if result == 300:
                print("  ✅ Test 1.4 PASSED: calculate_remaining(300, 0) = 300")
                task1_points += 5
            else:
                print(f"  ❌ Test 1.4 FAILED: Expected 300, got {result}")
            
        except Exception as e:
            print(f"  ❌ TASK 1 ERROR: {e}")
    
        print(f"  📊 Task 1 Score: {task1_points}/20 points")
        total_points += task1_points
    
        # Task 2 Tests
        print("\n📋 TASK 2: create_song")
        print("-" * 40)
        task2_points = 0
    
        try:
            result = create_song("Imagine")
            expected = {"title": "Imagine", "artist": "Unknown Artist", "duration": 180}
            if result == expected:
                print("  ✅ Test 2.1 PASSED: create_song('Imagine') uses defaults")
                task2_points += 7
            else:
                print(f"  ❌ Test 2.1 FAILED: Expected {expected}, got {result}")
        
            result = create_song("Yesterday", artist="The Beatles")
            expected = {"title": "Yesterday", "artist": "The Beatles", "duration": 180}
            if result == expected:
                print("  ✅ Test 2.2 PASSED: create_song('Yesterday', artist='The Beatles')")
                task2_points += 6
            else:
                print(f"  ❌ Test 2.2 FAILED: Expected {expected}, got {result}")
        
            result = create_song("Long Song", duration=600)
            expected = {"title": "Long Song", "artist": "Unknown Artist", "duration": 600}
            if result == expected:
                print("  ✅ Test 2.3 PASSED: create_song('Long Song', duration=600)")
                task2_points += 6
            else:
                print(f"  ❌ Test 2.3 FAILED: Expected {expected}, got {result}")
        
            result = create_song("Bohemian Rhapsody", artist="Queen", duration=354)
            expected = {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354}
            if result == expected:
                print("  ✅ Test 2.4 PASSED: create_song with all kwargs")
                task2_points += 6
            else:
                print(f"  ❌ Test 2.4 FAILED: Expected {expected}, got {result}")
            
        except Exception as e:
            print(f"  ❌ TASK 2 ERROR: {e}")
    
        print(f"  📊 Task 2 Score: {task2_points}/25 points")
        total_points += task2_points
    
        # Task 3 Tests
        print("\n📋 TASK 3: playlist_stats")
        print("-" * 40)
        task3_points = 0
    
        try:
            result = playlist_stats(180, 210, 240, 195)
            if result == (825, 4, 206.25):
                print("  ✅ Test 3.1 PASSED: playlist_stats(180, 210, 240, 195)")
                task3_points += 7
            else:
                print(f"  ❌ Test 3.1 FAILED: Expected (825, 4, 206.25), got {result}")
        
            result = playlist_stats(300, 300)
            if result == (600, 2, 300.0):
                print("  ✅ Test 3.2 PASSED: playlist_stats(300, 300)")
                task3_points += 6
            else:
                print(f"  ❌ Test 3.2 FAILED: Expected (600, 2, 300.0), got {result}")
        
            result = playlist_stats(240)
            if result == (240, 1, 240.0):
                print("  ✅ Test 3.3 PASSED: playlist_stats(240)")
                task3_points += 6
            else:
                print(f"  ❌ Test 3.3 FAILED: Expected (240, 1, 240.0), got {result}")
        
            result = playlist_stats()
            if result == (0, 0, 0.0):
                print("  ✅ Test 3.4 PASSED: playlist_stats() handles empty")
                task3_points += 6
            else:
                print(f"  ❌ Test 3.4 FAILED: Expected (0, 0, 0.0), got {result}")
            
        except Exception as e:
            print(f"  ❌ TASK 3 ERROR: {e}")
    
        print(f"  📊 Task 3 Score: {task3_points}/25 points")
        total_points += task3_points
    
        # Task 4 Tests
        print("\n📋 TASK 4: build_playlist")
        print("-" * 40)
        task4_points = 0
    
        try:
            result = build_playlist("Road Trip", song1=5, song2=10, song3=3)
            expected = {"name": "Road Trip", "songs": {"song1": 5, "song2": 10, "song3": 3}, "total_plays": 18}
            if result == expected:
                print("  ✅ Test 4.1 PASSED: build_playlist with multiple songs")
                task4_points += 8
            else:
                print(f"  ❌ Test 4.1 FAILED: Expected {expected}, got {result}")
        
            result = build_playlist("Chill Vibes", relaxing=20, ambient=15)
            expected = {"name": "Chill Vibes", "songs": {"relaxing": 20, "ambient": 15}, "total_plays": 35}
            if result == expected:
                print("  ✅ Test 4.2 PASSED: build_playlist('Chill Vibes', relaxing=20, ambient=15)")
                task4_points += 8
            else:
                print(f"  ❌ Test 4.2 FAILED: Expected {expected}, got {result}")
        
            result = build_playlist("Empty Playlist")
            expected = {"name": "Empty Playlist", "songs": {}, "total_plays": 0}
            if result == expected:
                print("  ✅ Test 4.3 PASSED: build_playlist('Empty Playlist') handles empty")
                task4_points += 7
            else:
                print(f"  ❌ Test 4.3 FAILED: Expected {expected}, got {result}")
        
            result = build_playlist("One Hit Wonder", hit_song=100)
            expected = {"name": "One Hit Wonder", "songs": {"hit_song": 100}, "total_plays": 100}
            if result == expected:
                print("  ✅ Test 4.4 PASSED: build_playlist('One Hit Wonder', hit_song=100)")
                task4_points += 7
            else:
                print(f"  ❌ Test 4.4 FAILED: Expected {expected}, got {result}")
            
        except Exception as e:
            print(f"  ❌ TASK 4 ERROR: {e}")
    
        print(f"  📊 Task 4 Score: {task4_points}/30 points")
        total_points += task4_points
    
        # Final Score
        print("\n" + "=" * 60)
        print(f"🏆 TOTAL SCORE: {total_points}/100 points")
        print("=" * 60)
    
        if total_points == 100:
            print("🌟 PERFECT SCORE! All solutions correct!")

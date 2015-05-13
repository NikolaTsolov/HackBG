import unittest
from MusicLibrary import Song, Playlist

class SongTest(unittest.TestCase):
    def setUp(self):
        self.my_song = Song("Solder Of Frortune", "Deep Purple", "Stormbringer", "3:14")
        self.second_song = Song("I Stand Alone", "Godsmack", "Awake", "4:30")
        self.rock = Playlist("Rock songs", repeat=True)
    def test_song_constructor(self):
        self.assertTrue(isinstance(self.my_song, Song))
        self.assertEqual(self.my_song.title, "Solder Of Frortune")
        self.assertEqual(self.my_song.artist, "Deep Purple")
        self.assertEqual(self.my_song.album, "Stormbringer")
        self.assertEqual(self.my_song.length, "3:14")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "3:65")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "63:45")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "45:63")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "1:63:45")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "1:43:65")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "10:00:00")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "1:4:253")
        with self.assertRaises(ValueError):
            other_song = Song("Knocking on your back door", "Deep Purple", "IDK", "1:433:15")

    def test_str_cast(self):
        self.assertEqual(str(self.my_song), "Solder Of Frortune - Deep Purple from Stormbringer - 3:14")

    def test_eq(self):
        self.assertTrue(self.my_song != self.second_song)
        self.assertTrue(self.my_song == self.my_song)

    def test_hash_cast(self):
        self.assertIsNotNone(hash(self.my_song))

    def test_duration(self):
        self.assertEqual(self.my_song.duration(seconds=True), 194)
        self.assertEqual(self.my_song.duration(minutes=True), 3)
        self.assertEqual(self.my_song.duration(hours=True), 0)
        self.assertEqual(self.my_song.duration(), "3:14")

    def test_playlist_constructor(self):
        self.assertTrue(isinstance(self.rock, Playlist))

    def test_add_song(self):
        self.rock.add_song(self.my_song)
        self.assertEqual(self.rock.playlist[0], self.my_song)

if __name__ == '__main__':
    unittest.main()

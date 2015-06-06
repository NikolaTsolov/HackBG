import unittest
from music_library import Song, Playlist
from music_library import NoSuchSong, NoMoreSongs

class SongTest(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("Solder Of Frortune", "Deep Purple", "Stormbringer", "3:14")
        self.second_song = Song("I Stand Alone", "Godsmack", "Awake", "4:30")

    def test_song_constructor(self):
        self.assertTrue(isinstance(self.my_song, Song))
        self.assertEqual(self.my_song.title(), "Solder Of Frortune")
        self.assertEqual(self.my_song.artist(), "Deep Purple")
        self.assertEqual(self.my_song.album(), "Stormbringer")
        self.assertEqual(self.my_song.length(), "3:14")


    def test_time_error(self):
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

class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("Solder Of Frortune", "Deep Purple", "Stormbringer", "3:14")
        self.second_song = Song("I Stand Alone", "Godsmack", "Awake", "4:30")
        self.rock = Playlist("Rock songs", True)
        self.songs = [self.my_song, self.second_song]
        self.rock.add_songs(self.songs)

    def test_playlist_constructor(self):
        self.assertTrue(isinstance(self.rock, Playlist))

    def test_add_song(self):
        self.assertEqual(self.rock.playlist, self.songs)

    def test_remove_song(self):
        self.rock.remove_song(self.my_song)
        self.assertEqual(self.rock.playlist, [self.second_song])

    def test_remove_song_fail(self):
        self.rock.remove_song(self.my_song)
        with self.assertRaises(NoSuchSong):
            self.rock.remove_song(self.my_song)

    def test_add_songs(self):
        self.assertEqual(self.rock.playlist, self.songs)

    def test_total_length(self):
        self.assertEqual(self.rock.total_length(), "0:07:44")

    def test_artists(self):
        histogram = {"Deep Purple": 1, "Godsmack": 1}
        self.assertEqual(self.rock.artists(), histogram)

    def test_repeat(self):
        self.assertEqual(self.rock.next_song(), self.my_song)
        self.assertEqual(self.rock.next_song(), self.second_song)
        self.assertEqual(self.rock.next_song(), self.my_song)

    def test_no_more_songs(self):
        self.rock.change_repeat(False)
        self.assertEqual(self.rock.next_song(), self.my_song)
        self.assertEqual(self.rock.next_song(), self.second_song)
        with self.assertRaises(NoMoreSongs):
            self.rock.next_song()
        self.rock.change_shuffle(True)
        self.rock.next_song()
        self.rock.next_song()
        with self.assertRaises(NoMoreSongs):
            self.rock.next_song()

    def test_shuffle(self):
        self.rock.change_shuffle(True)
        bard = Song("The Bard's Song", "Blind Guardian", "Somwhere Far Beyond", "3:28")
        self.rock.add_song(bard)
        a = self.rock.next_song()
        b = self.rock.next_song()
        c = self.rock.next_song()
        self.assertTrue(a != b and c != a and c != b)



if __name__ == '__main__':
    unittest.main()

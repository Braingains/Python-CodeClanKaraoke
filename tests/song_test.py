import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.Bohemian_Rhapsody = Song("Bohemian Rhapsody", "Queen", "Classic Rock")
        self.Africa = Song("Africa", "Toto", "Classic Rock")
        self.Wannabe = Song("Wannabe", "Spice Girls", "90s Pop")
        self.Never_Gonna_Give_You_Up = Song("Never Gonna Give You Up", "Rick Astley", "80s Pop")
        

    def test_song_has_title(self):
        self.assertEqual("Bohemian Rhapsody", self.Bohemian_Rhapsody.title)

    def test_song_has_artist(self):
        self.assertEqual("Africa", self.Africa.title)

    def test_song_has_genre(self):
        self.assertEqual("90s Pop", self.Wannabe.genre)
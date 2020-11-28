import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.Ewan = Guest("Ewan", 5)
        self.Shufan = Guest("Shufan", 50)
        self.Freddie = Guest("Freddie", 500)
        self.Mariah = Guest("Mariah", 5000)


    def test_guest_has_name(self):
        self.assertEqual("Ewan", self.Ewan.name)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.Shufan.wallet)
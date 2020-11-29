import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.Ewan = Guest("Ewan", 20, "Africa")
        self.Shufan = Guest("Shufan", 50, "Wannabe")
        self.Freddie = Guest("Freddie", 100, "Bohemian Rhapsody")
        self.Mariah = Guest("Mariah", 5000, "Never Gonna Give You Up")
        self.Floyd = Guest("Floyd", 150, "We Like To Party")
        self.Ross = Guest("Ross", 5, "Danger Zone")

        self.Large_Room = Room("Large Room", 12, 8, 0)
        self.Medium_Room = Room("Medium Room", 8, 10, 0)
        self.Small_Room = Room("Small Room", 4, 15, 0)

        self.Bohemian_Rhapsody = Song("Bohemian Rhapsody", "Queen", "Classic Rock")
        self.Africa = Song("Africa", "Toto", "Classic Rock")
        self.Wannabe = Song("Wannabe", "Spice Girls", "90s Pop")
        self.Never_Gonna_Give_You_Up = Song("Never Gonna Give You Up", "Rick Astley", "80s Pop")
        self.We_Like_To_Party = Song("We Like To Party", "Vengaboys", "90s Pop")
        self.Danger_Zone = Song("Danger Zone", "Kenny Loggins", "80s Pop")


    def test_guest_has_name(self):
        self.assertEqual("Ewan", self.Ewan.name)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.Shufan.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Africa", self.Ewan.favourite_song)

    def test_guest_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.Mariah.sufficient_funds(self.Large_Room))

    def test_guest_sufficient_funds__false_if_not_enough(self):
        self.assertEqual(False, self.Ross.sufficient_funds(self.Small_Room))

    def test_guest_can_pay_for_room__decreases_wallet(self):
        self.assertEqual(35, self.Shufan.pay_for_room(self.Small_Room))

    
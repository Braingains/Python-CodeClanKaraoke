import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.Ewan = Guest("Ewan", 20)
        self.Shufan = Guest("Shufan", 50)
        self.Freddie = Guest("Freddie", 100)
        self.Mariah = Guest("Mariah", 5000)
        self.Floyd = Guest("Floyd", 150)
        self.Ross = Guest("Ross", 5)

        self.Large_Room = Room("Large Room", 12, 8, 0)
        self.Medium_Room = Room("Medium Room", 8, 10, 0)
        self.Small_Room = Room("Small Room", 4, 15, 0)


    def test_guest_has_name(self):
        self.assertEqual("Ewan", self.Ewan.name)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.Shufan.wallet)

    def test_guest_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.Mariah.sufficient_funds(self.Large_Room))

    def test_guest_sufficient_funds__false_if_not_enough(self):
        self.assertEqual(False, self.Ross.sufficient_funds(self.Small_Room))

    def test_guest_can_pay_for_room__decreases_wallet(self):
        self.assertEqual(35, self.Shufan.pay_for_room(self.Small_Room))

    
import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.Large_Room = Room("Large Room", 12, 8, 0)
        self.Medium_Room = Room("Medium Room", 8, 10, 0)
        self.Small_Room = Room("Small Room", 4, 15, 0)

        self.Ewan = Guest("Ewan", 20)
        self.Shufan = Guest("Shufan", 50)
        self.Freddie = Guest("Freddie", 100)
        self.Mariah = Guest("Mariah", 5000)
        self.Floyd = Guest("Floyd", 150)
        self.Ross = Guest("Ross", 5)

        self.guests = []
        self.songs = []



    def test_room_has_name(self):
        self.assertEqual("Large Room", self.Large_Room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.Medium_Room.capacity)

    def test_room_has_fee(self):
        self.assertEqual(15, self.Small_Room.fee)

    def test_can_guest_afford_room__true_if_can(self):
        self.assertEqual(True, self.Small_Room.can_guest_afford_room(self.Ewan, self.Small_Room))

    def test_can_guest_afford_room__false_if_cannot(self):
        self.assertEqual(False, self.Small_Room.can_guest_afford_room(self.Ross, self.Small_Room))

    def test_check_in_guest(self):
        self.Small_Room.check_in_guest(self.Mariah, self.Small_Room)
        self.assertEqual(1, self.Small_Room.count_guests_in_room())

    #check out guests

    #add songs
import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.Large_Room = Room("Large Room", 12, 50, 0)
        self.Medium_Room = Room("Medium Room", 8, 40, 0)
        self.Small_Room = Room("Small Room", 4, 30, 0)

    def test_room_has_name(self):
        self.assertEqual("Large Room", self.Large_Room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.Medium_Room.capacity)

    def test_room_has_fee(self):
        self.assertEqual(30, self.Small_Room.fee)

    #check in guests

    #check out guests

    #add songs
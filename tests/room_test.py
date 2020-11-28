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

        self.Bohemian_Rhapsody = Song("Bohemian Rhapsody", "Queen", "Classic Rock")
        self.Africa = Song("Africa", "Toto", "Classic Rock")
        self.Wannabe = Song("Wannabe", "Spice Girls", "90s Pop")
        self.Never_Gonna_Give_You_Up = Song("Never Gonna Give You Up", "Rick Astley", "80s Pop")

        self.guests = []
        self.playlist = []



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

    def test_cannot_check_in_guest_with_insufficient_funds(self):
        self.Small_Room.check_in_guest(self.Ross, self.Small_Room)
        self.assertEqual(0, self.Small_Room.count_guests_in_room())

    def test_cannot_check_in_more_guests_than_room_capacity1(self):
        self.Small_Room.check_in_guest(self.Mariah, self.Small_Room)
        self.Small_Room.check_in_guest(self.Freddie, self.Small_Room)
        self.Small_Room.check_in_guest(self.Shufan, self.Small_Room)
        self.Small_Room.check_in_guest(self.Floyd, self.Small_Room)
        self.Small_Room.check_in_guest(self.Ewan, self.Small_Room)
        self.assertEqual(4, self.Small_Room.count_guests_in_room())


    def test_funds_added_to_till_at_check_in(self):
        self.Small_Room.check_in_guest(self.Mariah, self.Small_Room)
        self.assertEqual(15, self.Small_Room.till)

    def test_check_in_multiple_guests(self):
        self.Small_Room.check_in_guest(self.Mariah, self.Small_Room)
        self.Small_Room.check_in_guest(self.Freddie, self.Small_Room)
        self.Small_Room.check_in_guest(self.Shufan, self.Small_Room)
        self.Small_Room.check_in_guest(self.Floyd, self.Small_Room)
        self.assertEqual(4, self.Small_Room.count_guests_in_room())

    def test_check_out_guest1(self):
        self.Small_Room.check_in_guest(self.Freddie, self.Small_Room)
        self.Small_Room.check_out_guest(self.Freddie, self.Small_Room)
        self.assertEqual(0, self.Small_Room.count_guests_in_room())

    def test_check_out_guest2(self):
        self.Small_Room.check_in_guest(self.Mariah, self.Small_Room)
        self.Small_Room.check_in_guest(self.Freddie, self.Small_Room)
        self.Small_Room.check_out_guest(self.Freddie, self.Small_Room)
        self.assertEqual(1, self.Small_Room.count_guests_in_room())

    def test_songs_can_be_added_to_playlist(self):
        self.Small_Room.add_song_to_playlist(self.Africa)
        self.assertEqual(1, self.Small_Room.count_songs_in_playlist())

    def test_multiple_songs_can_be_added_to_playlist(self):
        self.Small_Room.add_song_to_playlist(self.Africa)
        self.Small_Room.add_song_to_playlist(self.Wannabe)
        self.assertEqual(2, self.Small_Room.count_songs_in_playlist())

    def test_songs_can_be_removed_from_playlist(self):
        self.Small_Room.add_song_to_playlist(self.Africa)
        self.Small_Room.add_song_to_playlist(self.Wannabe)
        self.Small_Room.remove_song_from_playlist(self.Wannabe)
        self.assertEqual(1, self.Small_Room.count_songs_in_playlist())

    
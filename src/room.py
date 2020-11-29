class Room:

    def __init__(self, name, capacity, fee, till):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.guests = []
        self.playlist = []

    def can_guest_afford_room (self, guest, name):
        return guest.sufficient_funds(name)

    def check_in_guest(self, guest, name):
        if self.can_guest_afford_room (guest, name) and self.count_guests_in_room() < self.capacity:
            self.till += self.fee
            self.guests.append(guest)

    def count_guests_in_room(self):
        return len(self.guests)

    def check_out_guest(self, guest, name):
        name.guests.remove(guest)

    def count_songs_in_playlist(self):
        return len(self.playlist)

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)

    def thats_my_jam(self, guest):
        for guest in self.guests:
            for song in self.playlist:
                if song == guest.favourite_song:
                    return ("THAT'S MY JAM!")
        return None



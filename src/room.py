class Room:

    def __init__(self, name, capacity, fee, till):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.guests = []
        self.songs = []

    def can_guest_afford_room (self, guest, name):
        return guest.sufficient_funds(name)

    def check_in_guest(self, guest, name):
        if self.can_guest_afford_room (guest, name):
            self.guests.append(guest)

    def count_guests_in_room(self):
        return len(self.guests)



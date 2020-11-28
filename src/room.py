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


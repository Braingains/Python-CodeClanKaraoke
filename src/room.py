class Room:

    def __init__(self, name, capacity, fee, till):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.guest = []
        self.songs = []
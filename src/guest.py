class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


    def sufficient_funds(self, room):
        return self.wallet >= room.fee

    def pay_for_room(self, room):
        if self.sufficient_funds(room):
            self.wallet -= room.fee
        return self.wallet
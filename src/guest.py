import pdb 
class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song


    def sufficient_funds(self, room):
        return self.wallet >= room.fee

    def pay_for_room(self, room):
        if self.sufficient_funds(room):
            self.wallet -= room.fee
        return self.wallet
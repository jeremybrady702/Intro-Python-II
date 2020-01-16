# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name="Player 1"):
        self.name = name
        self.room = room

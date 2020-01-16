from room import Room
from player import Player
# from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                     passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(input("Enter your character's name: "), room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print(room)
# * Waits for user input and decides what to do.


def userInput():
    uInput = input("What direction do you explore? (N, E, S, W): ")
    uInput = uInput.lower()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    valid_inputs = ["n", "e", "s", "w", "q"]
    if uInput not in valid_inputs:
        print("Sorry, that is not a valid direction, please choose N, E, S, or W")
        userInput()
    else:
        # pull down player
        global player
        if uInput == "q":
            print("Exiting...")
            exit()
        try:
            # North
            if uInput == "n":
                if player.room.n_to == "nothing":
                    print("Nothing to note here.")
                    userInput()
                else:
                    new_room = player.room.n_to
                    player = Player(new_room)
                    print(player.room)
                    userInput()
            # East
            if uInput == "e":
                if player.room.e_to == "nothing":
                    print("Nothing to note here.")
                    userInput()
                else:
                    new_room = player.room.e_to
                    player = Player(new_room)
                    print(player.room)
                    userInput()
            # South
            if uInput == "s":
                if player.room.s_to == "nothing":
                    print("Nothing to note here.")
                    userInput()
                else:
                    new_room = player.room.s_to
                    player = Player(new_room)
                    print(player.room)
                    userInput()
            # West
            if uInput == "w":
                if player.room.w_to == "nothing":
                    print("Nothing to note here.")
                    userInput()
                else:
                    new_room = player.room.w_to
                    player = Player(new_room)
                    print(player.room)
                    userInput()
        except AttributeError:
            print("Error, please try again")
            move()

# We're going to make a Haunted House classic text based game
#
# The user is going to stand outside a house and be given a choice to walk in
# Once they walk in, they're in a hall which leads to rooms in front (north), left (west), right (east), back (south)
# In the next version, we can add more rooms to a single room, right now there is going to be a kitchen,
# a dining room, a lounge, study
#
# There are many ways to do this, but each requires creating rooms and joining them somehow (linking them to each other).
#
# Each time the user walks into a room, the rooms' eerie description is read out.

class Room:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
    #enddef

    def getName(self):
        return self.__name
    #enddef

    def getDescription(self):
        return self.__description
    #enddef

    def getNorth(self):
        return self.__north
    #enddef

    def setNorth(self, room):
        self.__north = room
        if room.getSouth() != self:
            room.setSouth(self)
        #endif
    #enddef

    def getSouth(self):
        return self.__south
    # enddef

    def setSouth(self, room):
        self.__south = room
        if room.getNorth() != self:
            room.setNorth(self)
        #endif
    # enddef

    def getEast(self):
        return self.__east
    # enddef

    def setEast(self, room):
        self.__east = room
        if room.getWest() != self:
            room.setWest(self)
        #endif
    # enddef

    def getWest(self):
        return self.__west
    # enddef

    def setWest(self, room):
        self.__west = room
        if room.getEast() != self:
            room.setEast(self)
        #endif
    # enddef
#endclass

def askForNextRoom(room):
    print(room.getDescription())

    # find out what other rooms are available from this room
    # build a map of the exit: and its room reference
    # next, show the rooms to the user and ask which one they want
    # return the picked room from the map

    roomsAvailable = {

    }

    if room.getNorth() != None:
        roomsAvailable["North"] = room.getNorth()
    #endif

    if room.getSouth() != None:
        roomsAvailable["South"] = room.getSouth()
    #endif

    if room.getEast() != None:
        roomsAvailable["East"] = room.getEast()
    #endif

    if room.getWest() != None:
        roomsAvailable["West"] = room.getWest()
    #endif
    print("")

    print("The following rooms are available:")

    for r in roomsAvailable.keys():
        print(r)
    #endfor

    ans = input("Which room would you like to go to? Enter 'Q' to quit. ")

    if ans == "Q":
        return None
    #endif

    return roomsAvailable[ans]
#enddef

# Create rooms
outside = Room("Outside", "You are standing outside a haunted house,\nits decrepit silhouette etched against the dark sky as eerie whispers and the\ndistant echo of a child's laughter seep through the chilling breeze, urging you to step closer to its sinister embrace.")
hallway = Room("Hallway", "You are in the hallway of the haunted house, where the air is thick with the scent of mold and the faint sound of footsteps echoes from above, as if something unseen is always just a few paces ahead of you.")
kitchen = Room("Kitchen", "You are in the kitchen of the haunted house, where the air is stale with the aroma of long-spoiled feasts, and the clatter of utensils occasionally breaks the silence as shadows flicker across the walls like whispers of the past refusing to be still.")
livingRoom = Room("Living room", "You are in the living room of the haunted house, where the furniture is shrouded in dust covers that seem to breathe softly, and the faded portraits on the walls watch you with eyes that follow, their gazes piercing through the gloom.")
study = Room("Study", "You are in the study of the haunted house, where books with ancient, cracked spines line the shelves, a thick layer of dust undisturbed except for the fresh, solitary set of footprints that lead to a desk with an inkwell that still appears wet.")

# Link rooms
outside.setNorth(hallway)
hallway.setNorth(kitchen)
hallway.setWest(livingRoom)
hallway.setEast(study)


# Need a while loop until used quits
# The game starts with a Starting room. "CurrentRoom"

print("VELCOME TO ZE HAUNTED HAUS MUAHAHAHAHHAHAHAHAHAH")
print("")
currentRoom = outside

while currentRoom != None:
    currentRoom = askForNextRoom(currentRoom)
#endwhile

print("BOOOOO")
# One - to - One relationships
# One to Many


class Pond:
    def __init__(self, n):
        self.__name = n
        self.__fishes = []
    #enddef

    def getName(self):
        return self.__name
    #enddef

    def addFish(self, fish):
        # 1. If fish already belongs to another pond, from that pond remove this fish
        if fish.getPond() != None:
            fish.getPond().removeFish(fish)
        #endif

        # 2. Add it to this pond
        self.__fishes.append(fish)

        # 3. Tell the fish that it now belongs to this pond
        fish.setPond(self)
    #enddef

    def removeFish(self, fish):
        self.__fishes.remove(fish)

        fish.setPond(None)
    #enddef

    def countFish(self):
        return len(self.__fishes)
    #enddef

    def removeLastFish(self):
        self.__fishes.pop()
    #enddef
#endclass


class Fish:
    def __init__(self, n):
        self.__name = n
        self.__pond = None
    #enddef

    def getName(self):
        return self.__name
    #enddef

    def setPond(self, pond):
        self.__pond = pond

    def getPond(self):
        return self.__pond
    #enddef
#endclass

# 1976
sillyPond = Pond("silly pond")
goofyPond = Pond("goofy pond")

# 2016
fish1 = Fish("Bobby")
fish2 = Fish("Billy")

sillyPond.addFish(fish1)
sillyPond.addFish(fish2)

sillyPond.addFish(fish1)

print(f"{sillyPond.getName()} has {sillyPond.countFish()} fishies")

# You have added fish to the Pond. Pond now knows about its fishes. This is a ONE to MANY relationshop.
# You need to create a ONE to ONE reverse relationshop from the Fish back to the Pond. So we can get to the Pond from the Fish.

# Bobby belongs to silly pond

print(f"{fish1.getName()} belongs to {fish1.getPond().getName()}")
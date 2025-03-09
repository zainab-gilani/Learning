# Implement the Human class
# The human class will a property called `hasMakeupOn`
# doMakeup function should perform makeup and turn this on

# Name the Public properties AND functions

class Human:
    def __init__(self, name):
        self.__hasPerformedMakeup = False
        self.name = name
        self.hasMakeupOn = False
    #enddef

    # No underscore = Public. Accessible via dot notation.
    # 2 underscores = Private to the class instance. Accessible ONLY via methods of the instance.
    # 1 underscore  = Protected method or attribute

    def _thisIsProtected(self):
        pass

    def doMakeup(self):
        if self.__hasPerformedMakeup == True:
            print("How much makeup do you want to do man!?")
            return
        #endif

        self.__hasPerformedMakeup = True
        self.hasMakeupOn = True
    #enddef

    def speakAbout(self, anotherPerson):
        print(f"{anotherPerson.name} is my friend!")
    #enddef
#endclass


zainab = Human("Jolene")
print(f"Before makeup, does {zainab.name} have makeup on? {zainab.hasMakeupOn}")

zainab.doMakeup()
zainab.doMakeup()

print(f"After makeup, does {zainab.name} have makeup on? {zainab.hasMakeupOn}")

dolly = Human("Dolly")
zainab.speakAbout(dolly)


def countDown(num):
    if num == 0:
        return
    #endif

    print(num)
    countDown(num-1)

    print(f"This is after I printed the {num}")
#enddef

countDown(3)

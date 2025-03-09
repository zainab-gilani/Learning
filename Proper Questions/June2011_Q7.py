# Code uses type hints from Python 3.5 guys dw im not cheating

Names: [str] = ["Ben", "Thor", "Zoe", "Kate"]

Current: int = 0
Found: bool = False

PlayerName: str = input("What player are you looking for? ")

while not Found and Current < len(Names):
    if Names[Current] == PlayerName:
        Found = True
    else:
        Current += 1
    #endif
#endwhile

if Found:
    print("Yes, they have a top score")
else:
    print("No, they do not have a top score")
#endif
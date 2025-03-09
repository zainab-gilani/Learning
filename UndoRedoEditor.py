# Your challenge today is challenging.
# You must create a small journaling app that does the following:
# Prompts user to enter a few words to describe their day. They can write anything. However
# there's a special keyword that they might type and press enter:
#
# Undo
# Redo
# Show
# Stop
#
# Typing Undo should remove the last entry they wrote. The user may type undo multiple times in succession. Each time
# it undos and removes an entry, it should show what it removed.
# Typing Redo should put back the last entry that was undone. You cannot Redo something that was never Undone by the way.
#
# "Show" will show them all their entries. After each entry it keeps taking the next.


# entries = open("entries.txt", "a")
# wtv = input("Enter whatever: ")
# entries.write()
# entries.close()

def undo(list: [str]) -> str:
    entry = list.pop(-1)
    return entry
#enddef

def redo(list: [str], deleted: str):
    list.append(deleted)
#enddef

entries: [str] = []
deleted: [str] = []

print("1. Undo \n2. Redo \n3. Show \n4. Stop")

while True:
    entry: str = input("Enter a few words to describe your day: ").strip()
    if entry == "":
        continue
    #endif

    if entry.lower() == "undo":
        d = undo(entries)
        deleted.append(d)
        continue
    elif entry.lower() == "redo":
        d = deleted[-1]
        redo(entries, d)
        deleted.pop(-1)
        continue
    elif entry.lower() == "show":
        print(entries)
        continue
    elif entry.lower() == "stop":
        print(entries)
        exit()
    #endif

    entries.append(entry)
#endwhile
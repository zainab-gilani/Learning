import json

# DONE - Take tasks from the user
# DONE - ## Title, priority
# DONE - Save the tasks
# DONE - List the tasks
# DONE - List tasks nicely
# DONE - Allow completing tasks
# DONE - Allow changing priority

# Constants

TASK_FILE = "tasks.json"

# Global Variables

# A 2D array where each item is an array representing a task (with title and priority)
# [
#   ["Title here", 3]
# ]
tasks = []

# Functions

def showWelcome():
    if len(tasks) == 0:
        print("🎀 Welcome! 🎀\n")
    else:
        print("🎀 Welcome back! 🎀\n")
    #endif

    showStats()
    showListOfTasks()

    print("\n")
#enddef

def showStats():
    if len(tasks) == 0:
        # Nothing to do
        return
    #endif

    if len(tasks) == 1:
        print("You have 1 task remaining 😅")
    else:
        print("You have", len(tasks), "tasks remaining 😖")
    #endif
#endif

# Simply prints the task list beautifully like a girly code should
def showListOfTasks():
    count = 1

    for task in tasks:
        title = task[0]
        priority = task[1]
        symbol = ""

        if priority == 2:
            symbol = "! "
        elif priority == 3:
            symbol = "!! "
        elif priority == 4:
            symbol = "!!! "
        #endif

        line = str(count) + ". " + symbol + "✅ " + title

        print(line)

        count = count + 1
    #endfor
#enddef

def saveTasks():
    print("Debug: saveTasks()")

    file = open(TASK_FILE, 'w')

    # Each line in the file will be in the following format:
    # Title{|}Priority
    for task in tasks:
        title = task[0]
        priority = task[1]

        line = title + "{|}" + str(priority) + "\n"
        file.write(line)
    #endfor

    # json.dump(tasks, file)
    file.close()
#enddef

# Loads and returns tasks
def loadTasks():
    tasks = []
    try:
        file = open(TASK_FILE, "r")

        lines = file.readlines()

        # Title, Priority
        for i in range(0, len(lines)):
            line = lines[i]
            taskProps = line.strip().split("{|}")

            title = taskProps[0]
            priority = int(taskProps[1])

            task = [title, priority]
            tasks.append(task)
        #endfor

        # tasks = json.load(file)
        file.close()
    except:
        pass
    #endtry

    return tasks
#enddef

def addNewTask():
    title = input("Enter title: ")

    priority = 0
    while priority < 1 or priority > 4:
        priority = int(input("Enter priority between 1 (low) - 4 (high): "))

        if priority < 1 or priority > 4:
            print("Invalid choice. Try again.")
        #endif
    #endwhile

    task = [title, priority]
    tasks.append(task)

    saveTasks()

    print("\n\n")

    showListOfTasks()
#enddef

# Asks user a question and returns task number
def askForTaskNum(question):
    taskNum = 0

    while taskNum < 1 or taskNum > len(tasks):
        try:
            taskNum = int(input(question))
        except:
            print("Please enter a valid number.")
        #endtry
    #endwhile
    return taskNum
#enddef

def changePriority():
    # ask what to change it to
    # changes priority
    # saves tasks

    if len(tasks) == 0:
        print("There are no tasks to update.")
        return
    #endif

    showListOfTasks()

    taskNum = askForTaskNum("Which task would you like to update? ")

    newPriority = 0
    while newPriority < 1 or newPriority > 4:
        newPriority = int(input("Enter new priority between 1 (low) - 4 (high): "))

        if newPriority < 1 or newPriority > 4:
            print("Invalid choice. Try again.")
        #endif
    #endwhile

    # Update task's priority
    task = tasks[taskNum-1]
    task[1] = newPriority

    saveTasks()

    showStats()
    print()

#enddef

def markComplete():
    if len(tasks) == 0:
        print("There are no tasks to complete.")
        return
    #endif

    # Shows me the tasks (show list)
    # Asks which one?
    # removes the task
    # save tasks

    showListOfTasks()

    taskNum = askForTaskNum("Which task would you like to complete? ")

    tasks.pop(taskNum-1)

    saveTasks()

    showStats()
    print()
#enddef


def showMenu():
    print("You have the following choices:")
    print("1. Show list of tasks")
    print("2. Add a new task")
    print("3. Change the priority of a task")
    print("4. Mark a task as complete")
    print("5. Show me my stats")
    print("6. Quit")

    try:
        ans = int(input("What would you like to do? "))

        if ans == 1:
            showListOfTasks()
        elif ans == 2:
            addNewTask()
        elif ans == 3:
            changePriority()
        elif ans == 4:
            markComplete()
        elif ans == 5:
            showStats()
        elif ans == 6:
            exit()
        else:
            print("\n\nThere is no such choice. Try again.\n")
            showMenu()
        #endif
    except ValueError:
        print("Not a number!")
        showMenu()
    #endtry
#enddef

def startApp():
    while True:
        showMenu()
    #endwhile
#enddef

# Main Program
tasks = loadTasks()

showWelcome()

startApp()



# We already have learned to use Classes
# We're going to structure and create our own class called Stack
# Inside under the hood, we're going to use a normal Python List for storage
# We're going to support all the methods a stack must offer:

# DONE 1. push
# DONE 2. pop
# 3. Is Empty
# 4. Is Full (only if a size was given for the stack)
# DONE 5. Peek
# 6. Size

class Stack:
    def __init__(self, size = None):
        self.__stack = []
        self.__size = size
    #enddef

    def push(self, item):
        if self.isFull():
            return
        self.__stack.append(item)
    #enddef

    def peek(self):
        if self.isEmpty():
            return None
        #endif
        return self.__stack[-1]
    #enddef

    def pop(self):
        if self.isEmpty():
            return None
        #endif

        return self.__stack.pop()
    #enddef

    def isEmpty(self):
        if len(self.__stack) == 0:
            return True
        #endif
        return False
    #enddef

    def isFull(self):
        if self.__size == None:
            return False
        #endif

        if len(self.__stack) == self.__size:
            return True
        #endif

        return False
    #enddef
#endclass


stack = Stack()
stack.push("First")
stack.push("Second")
stack.push("Third")

print(stack.peek())



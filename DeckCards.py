front = 1
rear = 52
queue = (rear - front) + 1

def dealCard():
    currentCard = front

    # Move the front pointer to next card
    front = front + 1

    # Reset front to point to rear card if it's now pointing to a non existent card
    if front > rear:
        front = rear
        return None
    #endif

    queue = (rear - front) + 1

    return currentCard
#endidef



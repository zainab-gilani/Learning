numbers = [1, 5, 2, 7, 9, 4, 6]

def mergeSort(numlist: list) -> list:
    # Returns list if it only contains one or fewer elements
    if len(numlist) <= 1:
        return numlist
    #endif

    # Calculates middle, left side, and right side of the list
    mid = len(numlist) // 2
    left = numlist[:mid]
    right = numlist[mid:]

    # Recursive
    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)
#enddef

def merge(left: list, right: list) -> list:
    newlist = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            newlist.append(left[i])
            i += 1
        else:
            newlist.append(right[j])
            j += 1
        #endif
    #endwhile
    newlist.extend(left[i:])
    newlist.extend(right[j:])

    return newlist
#enddef

print(f"Unsorted list: {numbers}")

sorted = mergeSort(numbers)
print(f"Sorted list: {sorted}")
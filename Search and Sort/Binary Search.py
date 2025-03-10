numbers = [1, 2, 5, 6, 7, 9]
target = int(input("Enter a target number: "))

def binarySearch(numlist, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low+high) // 2
        if numlist[mid] == target:
            return mid
        elif target < numlist[mid]:
            high = mid - 1
        else:
            low = mid + 1
        #endif
    #endwhile
    return None
#enddef

index = binarySearch(numbers, target)

if index != None:
    print(f"Target found at position {index}")
#endif
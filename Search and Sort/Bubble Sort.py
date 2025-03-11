def bubbleSort(numlist):
    for i in range(len(numlist) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if numlist[j] > numlist[j + 1]:
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
                swapped = True
            #endif
        #endfor
        if not swapped:
            break
        #endif
    #endfor
#enddef

numbers = [1, 5, 2, 7, 9, 4, 6]
print(f"Unsorted list: {numbers}")

bubbleSort(numbers)

print(f"Sorted list: {numbers}")
# Linear search

numbers = [1, 2, 5, 6, 7, 9]
target = int(input("Enter a target number: "))
found = False

for i in range(len(numbers)):
    num = numbers[i]
    if num == target:
        found = True
        print(f"Number found in position {i+1}")
    # endif
#endfor

if found == False:
    print("Target not in list.")
#endif
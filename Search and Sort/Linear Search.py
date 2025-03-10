# Linear search

numbers = [1, 2, 5, 6, 7, 9]
target = int(input("Enter a target number: "))
found = False

for num in numbers:
    if num == target:
        found = True
        print("Number found")
    #endif
#endfor

if found == False:
    print("Number not in list.")
#endif
# Your next mission, Ethan Hunt, whether you choose to accept or not is
# to find the second largest number in a list of numbers given by the user comma separated of course
# So: 1,4,5,3,6,2 would find the second largest to be 5
#
# You cannot use sort() or max() or other system built in methods. The list
# Could be unsorted in any order and length given to you. Use your bloody head.

# 3,2,4,7,7,8,3,8,2,1,9,5,2,6

nums = input("Enter a comma separated list of numbers: ")
nums = nums.replace(" ", "")

numbers = nums.split(",")

num_list = []

for num in numbers:
    num_list.append(int(num))

print(num_list)

largest = 0
second_largest = 0
third_largest = 0

for i in range(len(num_list)):
    current = num_list[i]

    if current > largest:
        third_largest = second_largest

        second_largest = largest

        largest = current
    #endif
#endfor

print(largest)
print(second_largest)
print(third_largest)
# You'll be given a set of numbers:
# 1, 1, 4, 3, 4, 4, 4, 2, 1, 3, 4
#
# Find and list all duplicates like:
#
# [[1, 1, 1], [2], [3, 3], [4, 4, 4, 4]]

nums = input("Enter a comma separated list of numbers: ").strip()
nums = nums.replace(" ", "")

count = {}
numbers = nums.split(",")

# USING DICTIONARIES
# print(numbers)

for i in range(len(numbers)):
    num = numbers[i]

    if num not in count.keys():
        count[num] = []
    #endif

    count[num].append(num)
#endfor

print(count)

list_of_nums = []

for l in count:
    value = count[l]
    list_of_nums.append(value)
#endfor

print(list_of_nums)

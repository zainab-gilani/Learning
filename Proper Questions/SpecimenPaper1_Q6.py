num = int(input("Enter a number: "))
binary = []
result = -1

while result != 0:
    remainder = num % 2
    result = num // 2
    num = result

    binary.insert(0, str(remainder))
#endwhile

print("".join(binary))
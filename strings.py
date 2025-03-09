def count_letters(word, d):
    for i in range(len(word)):
        char = word[i]

        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
        # endif
    # endfor
# enddef

first = input("Enter a word: ")
second = input("Enter another word: ")

first_characters = {}
second_characters = {}

count_letters(first, first_characters)
count_letters(second, second_characters)

can_use = []

for c in first_characters:
    if c in second_characters and first_characters[c] <= second_characters[c]:
        can_use.append(c)
    # endif
# endfor

if len(can_use) == len(first_characters):
    print("First word can be created using second word.")
else:
    print("First word cannot be created using second word.")
# endif
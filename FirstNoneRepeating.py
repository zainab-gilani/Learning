# Ask the user for some kind of a string which has repeated characters, like:
# aabbccddeefgg
# abba
# aaba
#
# Your mission, whether you choose to accept or not, is to:
# * Find the FIRST character that is NOT repeating
#
# Okay that's it for now kiddie
# You are not allowed to use:
# * Dictionaries
# * Any built-in python method
# * Use a single loop no more than one loop in TOTAL allowed to solve this problem


word = input("Enter a word: ")

non_repeating_letter = ""

for i in range(len(word)):
    if len(word) == 1:
        non_repeating_letter = word[i]
        break
    #endif

    if i == 0 and word[i] != word[i+1]:
        non_repeating_letter = word[i]
        break
    #endif

    if i == len(word) - 1 and word[i] != word[i-1]:
        non_repeating_letter = word[i]
        break
    #endif

    if word[i] != word[i+1] and word[i] != word[i-1]:
        non_repeating_letter = word[i]
        break
    #endif
#endfor

if non_repeating_letter != "":
    print(non_repeating_letter)
#endif
vowels: [str] = ["a", "e", "i", "o", "u"]

def get_characters(string: str) -> [str]:
    list: [str] = []
    for i in string:
        list.append(i)
    #endfor
    return list
#enddef

def get_indexes(string: str) -> [int]:
    indexes = []
    for i in range(len(string)):
        letter = string[i]
        if letter in vowels:
            indexes.append(i)
        #endif
    #endfor
    return indexes
#enddef

def get_new_word(characters: [str], indexes: [int]) -> str:
    last = -1
    for i in range(len(indexes) // 2):
        n = indexes[i]

        temp = characters[n]
        # print(temp, n, last)
        characters[n] = characters[indexes[last]]
        # print(characters[n], n, last)
        characters[indexes[last]] = temp
        # print(characters[indexes[last]], n, last)
        last -= 1
    #endfor

    return "".join(characters)
#enddef

string = input("Enter a word: ")

characters = get_characters(string)

indexes = get_indexes(string)

word = get_new_word(characters, indexes)

print(word)
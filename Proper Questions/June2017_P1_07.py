word = input("Enter a word: ").upper()

characters = {}

for i in range(len(word)):
    char = word[i]

    if char not in characters:
        characters[char] = 1
    else:
        characters[char] += 1
    #endif
#endfor

words: [str] = []

for char in characters:
    phrase = f"{char} {characters[char]}"

    words.append(phrase)
#endfor

compressed = ", ".join(words)

print(compressed)
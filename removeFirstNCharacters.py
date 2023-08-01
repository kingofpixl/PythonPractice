#Write a program to remove characters from a string starting from zero up to n and return a new string.

userString = input('Enter your Word ')
nValue = input('how many letters do you want to cut off ')

nValue = int(nValue)

def removeNCharacters(word, n):
    print('Original String: ', word)
    return word[n:]

print(removeNCharacters(userString, nValue))
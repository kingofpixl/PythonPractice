number = input("Enter a number (1234): ")
map = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
}
words = ""
for character in number:
    words += map.get(character, "!") + " "
print(words)
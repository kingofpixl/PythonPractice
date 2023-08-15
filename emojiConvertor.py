def emojiConvertor(userInput):
    words = userInput.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
    
    
message = input("enter your message with a emoji: ")
print(emojiConvertor(message))

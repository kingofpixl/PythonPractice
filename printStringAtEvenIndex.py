#Write a program to accept a string from the user and display characters that are present at an even index number.

userInput = input('Enter Your Word ')

inputlength = len(userInput)

#prints at a even index number
for i in range(0, inputlength-1, 2):
    print(userInput[i])
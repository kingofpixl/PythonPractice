#Write a program to find how many times substring “Emma” appears in the given string.

String = "Emma is good developer. Emma is a writer"
#string = input('Enter a string to look through: ')

lookingFor = 'Emma'
#lookingFor = input('Enter the word you are looking for: ')

counter = String.count(lookingFor)

print(lookingFor, 'appeared', counter, 'times')
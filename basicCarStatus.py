userInput = ""
while True:
    userInput = input("please type in a command (help, start, stop, quit) ").lower()
    if userInput == "help":
        print('''
              start - to start the car
              stop - to stop the car
              quit - to exit the program
              ''')
    elif userInput == "start":
        print("Car started...Ready to go!")
    elif userInput == "stop":
        print("Car stopped.")
    elif userInput == "quit":
        break
    else:
        print("Please enter in a valid input")
    
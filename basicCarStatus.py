userInput = ""
started = False
while True:
    userInput = input("please type in a command (help, start, stop, quit) ").lower()
    if userInput == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit the program
              ''')
    elif userInput == "start":
        if started == False:
            started = True
            print("Car started...Ready to go!")
        else:
            print("Car is already Started")
    elif userInput == "stop":
        if started == True:
            started = False
            print("Car stopped.")
        else:
            print("Car is already stopped")
    elif userInput == "quit":
        break
    else:
        print("Please enter in a valid input")
    
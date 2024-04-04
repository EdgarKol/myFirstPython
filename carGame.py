command = ""
started = False
while True:
    command = input("> ").lower()
    if command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started....Lets go")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("I dont understand that...")

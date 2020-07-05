command = ""
isCarStarted = False
while True:
        command = input("> ").lower()

        if command == "start":
            if isCarStarted:
                print("Car is alreadyy STARTED....")
            else:
                print("Car started....")
                isCarStarted = True
        elif command == "stop":
            if not isCarStarted:
                print("Car is alreadyy STOPED....")
            else:
                print("Car stoped....")
                isCarStarted = False
        elif command == "help":
            print("start - start the car")
            print("stop - stop the car")
            print("quit - to exit")
        elif command == "quit":
            break
        else:
            print("I dont understand that")

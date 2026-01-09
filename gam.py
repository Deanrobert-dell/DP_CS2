def startgame():
    global room1, room2, room3, room4, room5, room6, room7, roomSecret, roomBoss
    while True:
        print("You enter the pyramid, and the opening behind you crumbles shut, you are stuck")
        print("You had been exploring near a pyramid when you found a small entrance and went inside.")
        play = input("Do you wish to continue? (Y/N): ").upper()
        if play == "Y":
            room1_func()
            break
        elif play == "N":
            print("BYE BYE")
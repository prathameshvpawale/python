choice = "-"

while True:
    if choice == "0":
        break
    elif choice in "12345":
        print("youe choice {}".format(choice))
    else:
        print("1 .go to sleep")
        print("2 .go to sleep")
        print("3 .go to sleep")
        print("4 .go to sleep")
        print("5 .go to sleep")
    choice = input()
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "12345":
        print("adding {}" .format(current_choice))
        if current_choice == "1":
            computer_parts.append("moniter")
        elif current_choice =="2":
            computer_parts.append("keyboard")
        elif current_choice =="3":
            computer_parts.append("mouse")
        elif current_choice =="4":
            computer_parts.append("cpu")
        elif current_choice =="5":
            computer_parts.append("cpu")
    else:
        print("please add option from below list")
        print("1 moniter")
        print("2 keyboard")
        print("3 mouse")
        print("4 cpu")
        print("5 gpu")
        print("exit")
    current_choice = input()

print(computer_parts)

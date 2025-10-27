current_choice = "-"
computer_parts = []
availabal_parts = [
    "moniter",
    "kayboard",
    "mouse",
    "cpu",
    "sound",
    "mouse pad",
    "ssd",
    "mother board",
    "gpu"]
# vaild_choices = [ str(i) for i in range(1, len(availabal_parts)+1)]
vaild_choices = []
for i in range (1 ,len(availabal_parts) + 1):
    vaild_choices.append(str(i))
print(vaild_choices)
while current_choice != '0':
    if current_choice in vaild_choices:
        print("adding {}" .format(current_choice))
        index = int (current_choice) -1
        chosen_parts = availabal_parts[index]
        computer_parts.append(chosen_parts)
    else:
        print("please add option from below list")
        for number , part in enumerate(availabal_parts):
            print("{0}: {1}".format(number + 1 , part))
    current_choice = input()

print(computer_parts)

menu_options = {
    "1": "Go to sleep",
    "2": "Read a book",
    "3": "Do exercise",
    "4": "Eat something",
    "5": "Watch a movie",
}

def show_menu():
    print("\nPlease choose an option:")
    for key, text in sorted(menu_options.items()):
        print(f"{key}. {text}")
    print("0. Exit")

def handle_choice(choice: str) -> bool:
    choice = choice.strip()
    if choice == "0":
        print("Goodbye!")
        return False
    if choice in menu_options:
        print(f"You chose {choice}: {menu_options[choice]}")
        return True
    print(f"Invalid choice: {choice!r}. Enter a number 0-5.")
    return True

def main() -> None:
    try:
        running = True
        while running:
            show_menu()
            choice = input("Enter choice (0 to exit): ")
            running = handle_choice(choice)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")

if __name__ == "__main__":
    main()
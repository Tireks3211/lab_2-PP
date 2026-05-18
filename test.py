<<<<<<< HEAD
print("world")
=======
print("Hello")
>>>>>>> develop
def display_string(text: str) -> None:
    #The function takes a text string and prints it to the console using print()
    """Prints the given string."""
    print(text)

def main() -> None:
    user_input = input("Enter a string: ")
    display_string(user_input)

if __name__ == "__main__":
    main()
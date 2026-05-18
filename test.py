def display_string(text: str) -> None:
    """Prints the given string."""
    print(text)

def main() -> None:
    user_input = input("Enter a string: ")
    display_string(user_input)

if __name__ == "__main__":
    main()
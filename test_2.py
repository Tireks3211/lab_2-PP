def count_words(text: str) -> int:
    #The function takes a text string and splits it into words by spaces using split()
    #and returns the number of words received as an integer
    """Returns the number of words in the given string."""
    words = text.split()
    return len(words)

def main() -> None:
    user_input = input("Enter a string: ")
    word_count = count_words(user_input)
    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    main()
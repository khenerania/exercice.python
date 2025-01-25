def save_unique_words(unique_words):
    filename = input("Enter filename to save unique words: ")
    with open(filename, 'w') as file:
        for word in sorted(unique_words):
            file.write("%s\n" % word)
    print(f"Unique words saved to {filename}.")

def main():
    unique_words = set()
    total_words = 0

    while True:
        word = input("Enter a word: ").strip()
        total_words += 1
        word_lower = word.lower()
        if word_lower in unique_words:
            print(f"You typed in {len(unique_words)} unique words out of {total_words} total words.")
            break
        unique_words.add(word_lower)

    print("Unique words (alphabetically):", sorted(unique_words))
    save_unique_words(unique_words)

if __name__ == "__main__":
    main()


from stats import n_words, get_count_letters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        text = get_book_text(sys.argv[1])
        print(f"Found {n_words(text)} total words")

        letter_frequency = get_count_letters(text)
        for key in sort_dict(letter_frequency):
            if key.isalpha():
                print(f"{key}: {letter_frequency[key]}")

main()
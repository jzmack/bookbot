from stats import count_words, count_letters, sort_letters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    file = sys.argv[1]

    print(f"Analyzing book found at {file}...")
    text = get_book_text(file)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    letter_count = count_letters(text)
    sorted_letters = sort_letters(letter_count)

    for char_dict in sorted_letters:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
        

main()

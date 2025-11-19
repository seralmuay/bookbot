import sys

from stats import get_num_words, count_characters, sort_character_counts

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
    
def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        if entry['char'].isalpha():  # Only print alphabetic characters
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
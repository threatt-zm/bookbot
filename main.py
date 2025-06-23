import sys
from stats import get_word_count, get_char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_char_count(book_text)
    sorted_dict = sort_dict(num_chars)
    for d in sorted_dict:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()
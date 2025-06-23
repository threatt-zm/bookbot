from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #print(book_text)
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    num_chars = get_char_count(book_text)
    print(num_chars)

main()
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #print(book_text)
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")

main()
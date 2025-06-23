def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters
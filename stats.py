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

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    ls = []
    for k, v in dictionary.items():
        d={}
        d["char"] = k
        d["num"] = v
        ls.append(d)
    ls.sort(reverse=True, key=sort_on)
    return ls
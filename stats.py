def get_word_count(filepath):
    words = filepath.split()
    count = len(words)
    return count

def get_char_count(filepath):
    text = filepath.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(list_count):
    sorted = {
        "char": "",
        "nums": ""
    }
    for char in list_count:
            
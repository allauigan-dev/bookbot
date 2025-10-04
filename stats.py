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
    char_list = [{"char":c, "num": n} for c, n in list_count.items()]

    def get_num(a):
        return a["num"]
    
    char_list.sort(key=get_num, reverse=True)

    return char_list
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    # use the relative path to your frankenstein.txt file
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    # print(text)
    word_count = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    print(char_count)
    sort = sort_char_count(char_count)
    print(sort)

# call main() to run the program
if __name__ == "__main__":
    main()

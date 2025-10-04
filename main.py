import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    # use the relative path to your frankenstein.txt file
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    # print(text)
    word_count = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    # print(char_count)
    sort = sort_char_count(char_count)
    for item in sort:
        if item["char"].isalpha():
              print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

# call main() to run the program
if __name__ == "__main__":
    main()

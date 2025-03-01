import sys
from stats import count_chars, count_words, sort_count


def get_book_text(filepath: str):
    book = ""
    with open(filepath) as f:
        book = f.read()
    return book


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return 1
    filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    book = get_book_text(filename)
    print("----------- Word Count ----------")
    count = count_words(book)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    chars = count_chars(book)
    sorted_chars = sort_count(chars)
    for sorted in sorted_chars:
        print(f"{sorted[0]}: {sorted[1]}")
    print("============= END ===============")


main()

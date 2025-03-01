def count_words(book: str):
    count = len(book.split())
    return count


def count_chars(book: str):
    count: dict[str, int] = {}
    for word in book.split():
        for letter in word:
            lower = letter.lower()
            if lower not in count:
                count[lower] = 1
            else:
                count[lower] += 1
    return count


def sort_count(count: dict[str, int]):
    sorted_count = sorted(count.items(), reverse=True, key=lambda x: x[1])
    return sorted_count

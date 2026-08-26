from stats import get_book_wordcount, get_character_count, chars_dict_to_sorted_list
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def print_report(bookPath: str, wordCount: int, sortedList: list[tuple[str, int]]) -> None:
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookPath}...')
    print('----------- Word Count ----------')
    print(f'Found {wordCount} total words')
    print('--------- Character Count -------')
    for item in sortedList:
        if item[0].isalpha():
            print(f'{item[0]}: {item[1]}')
    print('============= END ===============')


def main():
    book = get_book_text(sys.argv[1])
    charCount = get_character_count(book)
    sortedCount = chars_dict_to_sorted_list(charCount)
    print_report('books/frankenstein.txt', get_book_wordcount(book), sortedCount)




if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
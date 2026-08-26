def get_book_wordcount(book: str) -> int:
    words = book.split()
    return len(words)

def get_character_count(book: str) -> dict[str, int]:
    book = book.lower()
    char_dict: dict[str, int] = {}
    for character in book:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def sort_on(charList: tuple[str, int]) -> int:
    return charList[1]

def chars_dict_to_sorted_list(charsDict: dict[str, int]) -> list[tuple[str, int]]:
    sortedList: list[tuple[str, int]] = []
    for key in charsDict:
        sortedList.append((key, charsDict[key]))
    sortedList = sorted(sortedList, reverse=True, key=sort_on)
    return sortedList

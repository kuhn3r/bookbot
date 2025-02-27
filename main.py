from stats import count_words, get_chars_dict

def get_book_text():
    with open("books/frankenstein.txt") as words:
        book = words.read()
    return book

def main():
    book_text = get_book_text()
    num_words = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    print(f"{num_words} words found in the document")
    print(chars_dict)
main()
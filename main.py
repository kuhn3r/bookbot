from stats import count_words

def get_book_text():
    with open("books/frankenstein.txt") as words:
        book = words.read()
    return book

def main():
    book_text = get_book_text()
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()
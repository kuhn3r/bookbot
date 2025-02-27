from stats import count_words, get_chars_dict, chars_dict_sorted
import sys

def main():
    if len(sys.argv) != 2:  
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted = chars_dict_sorted(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
def get_book_text(book_path):
    with open(book_path) as words:
        book = words.read()
    return book


   

main()
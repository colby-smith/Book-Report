def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    display_book(text)
    
def get_book_text(path):
    with open (path) as book:
        return book.read()

def display_book(text):
    print (text)

main()
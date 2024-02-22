def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    
    display_book(text)
    count_Words(words)


def get_book_text(path):
    with open (path) as book:
        return book.read()

def display_book(text):
    print (text)

def count_Words(words):
    word_count = 0
    for word in words:
        word_count += 1
    print (word_count)

main()
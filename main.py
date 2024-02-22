import time
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()

    create_report(book_path, count_Words(words))

def get_book_text(path):
    with open (path) as book:
        return book.read()

def display_book(text):
    print (text)

def count_Words(words):
    word_count = 0
    for word in words:
        word_count += 1
    return (word_count)

def count_characters(text):
    chars_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars_count:
            chars_count[lowered] += 1
        else:
            chars_count[lowered] = 1
    return (chars_count)


def create_report(book_path, word_count):
    print ("--------------------------------------------------")
    print (f"   Beginning report of {book_path}    ")
    print ("--------------------------------------------------")
    print (f"     There is {word_count} words in this document")
    print ("--------------------------------------------------")
    



main()
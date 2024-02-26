def main():
    book_path = "books/text.txt"
    text = get_book_text(book_path)
    words = text.split()
    chars_dict = count_characters(text)
    word_count = count_Words(words)
    sorted_chars_list = dict_to_List(chars_dict)
    
    create_report(book_path, word_count, sorted_chars_list)
    
    
    
### Allows us to create the 'text' variable in main to open the book via it's path. ###
def get_book_text(path):
    with open (path) as book:
        return book.read()

### displays the chosen text to the console. ###
def display_book(text):
    print (text)
    
### Counts the number of words contained in the 'text'. ###
def count_Words(words):
    word_count = 0
    for word in words:
        word_count += 1
    return (word_count)

### Counts the number of characters in the 'text' and stores them in a dictionary. ###
def count_characters(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return (chars_dict)

def sort_on(d):
    return d["num"]

def dict_to_List(num_chars_dict):
    sorted_chars_list = []
    for ch in num_chars_dict:
        sorted_chars_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_chars_list.sort(reverse=True, key=sort_on)
    return sorted_chars_list

### Displays a report on the 'text' to the console using the various functions above. ###
def create_report(book_path, word_count, sorted_chars_list):
    print ("--------------------------------------------------")
    print (f"   Beginning report of {book_path}    ")
    print ("--------------------------------------------------")
    print (f"     There is {word_count} words in this document")
    print ("--------------------------------------------------")
    print ()
    
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print ("-------------------------------------------------------------------------")
        print (f"     The '{item["char"]}' character was found '{item['num']}' times!")
        print ("-------------------------------------------------------------------------")
    print ("-------------------------------------------------------------------------")
    print ("................................End Report...............................")
    print ("-------------------------------------------------------------------------")

    

















main()
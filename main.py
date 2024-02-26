def main():
    book_path = "books/text.txt"
    text = get_book_text(book_path)
    words = text.split()
    chars_dict = count_characters(text)
    word_count = count_Words(words)
    sorted_chars_list = dict_to_List(chars_dict)
    create_report(book_path, word_count, sorted_chars_list)

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

def create_report(book_path, word_count, sorted_chars_list):
    print ("--------------------------------------------------")
    print (f".....Beginning report of {book_path}.....")
    print ("--------------------------------------------------")
    print (f".....There is {word_count} words in this document.....")
    # print ("--------------------------------------------------")
    
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print (f"-------------------------------------------------------")
        print (f".....The '{item["char"]}' character was found '{item['num']}' times!.....")
        # print ("-------------------------------------------------------------------------")
    print ("-------------------------------------------------------")
    print (".......................End Report......................")
    print ("-------------------------------------------------------")

main()
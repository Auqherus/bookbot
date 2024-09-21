def main():
     book_path = "/home/auqherus/workspace/github.com/Auqherus/bookbot/books/frankenstein.txt"
     path = path_to_document(book_path) # it's a path with file contents(book)
     words_number = count_words(path) #its a number = 77986
     char_dict = count_char(path)
     log_message(words_number, char_dict)
   
    
def path_to_document(path): #it is done

    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text): # it is done

    book_text = text.split()
    number = 0
    for word in book_text:
        number+=1
    #print(number)
    return number


def count_char(text): # it is done
    
    dict_with_counted_chars = {}
    book_text = text.lower()

    for char in book_text:
        if char in dict_with_counted_chars:
            dict_with_counted_chars[char] += 1
        elif char not in dict_with_counted_chars:
             dict_with_counted_chars[char] = 1

    #print(dict_with_counted_chars)
    return dict_with_counted_chars


def log_message(word_count, char_count): # it is done
     
     list_from_dictionary = []
     
     print("--- Begin report of books/frankenstein.txt ---\n")
     print(f"{word_count} words was found in the document")\

     for key, char in char_count.items(): # done with making list of dictionares
         if key.isalpha():
            list_from_dictionary.append({key:char})

     list_from_dictionary.sort(key=lambda x: list(x.values())[0], reverse=True) # done with sorting list from highest to lowest

     #print(list_from_dictionary)

     for word in list_from_dictionary:
         char = list(word.items())[0][0]
         value = list(word.items())[0][1]
         print(f"The '{char}' character was found {value} times")

     print("\n--- End report of books ---")








     return None
      

main()
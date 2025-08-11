from stats import get_word_count, get_character_count_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    return None

def main():
   words = get_book_text("books/frankenstein.txt")
   word_count = get_word_count(words)
   character_count_dict = get_character_count_dict(words)

   print(f"{word_count} words found in the document")
   print(f"{character_count_dict} characters found")
   
main()
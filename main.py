from stats import get_word_count, get_characters, sort_characters, filter_non_alphabet

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    return None

def print_characters(characters):
    print("--------- Character Count -------")

    for character in characters:
        char = character["char"]
        num = character["num"]
        print(f"{char}: {num}")

def print_report(book, word_count, characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print_characters(characters)
    print("============= END ===============")

def main():
   book = "books/frankenstein.txt"
   words = get_book_text(book)
   word_count = get_word_count(words)
   characters = get_characters(words)
   characters = filter_non_alphabet(characters)
   sort_characters(characters)
   print_report(book, word_count, characters)
   
main()
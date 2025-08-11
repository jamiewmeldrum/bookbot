from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    return None

def main():
   words = get_book_text("books/frankenstein.txt")
   word_count = get_word_count(words)
   print(f"{word_count} words found in the document")

main()
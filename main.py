from stats import book_word_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  path = "books/frankenstein.txt"
  contents = get_book_text(path)
  word_count = book_word_count(contents)
  print(f"{word_count} words found in the document")

main()
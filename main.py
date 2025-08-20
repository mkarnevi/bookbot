import sys
from stats import book_word_count, book_character_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["number"]

def convert_and_sort_dictionary(dictionary):
  unsorted_dictionary_list = [{"char": character, "number": number} for character, number in dictionary.items()]

  unsorted_dictionary_list.sort(reverse=True, key=sort_on)
  return unsorted_dictionary_list

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  path = sys.argv[1]
  
  #path = "books/frankenstein.txt"
  contents = get_book_text(path)
  word_count = book_word_count(contents)
  
  dictionary = book_character_count(contents)
  sorted_dictionary = convert_and_sort_dictionary(dictionary)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for entry in sorted_dictionary:
    if entry["char"].isalpha():
      print(f"{entry['char']}: {entry['number']}")
  print("============= END ===============")

main()
def book_word_count(contents):
  return len(contents.split())

def book_character_count(contents):
  characters_dict = {}
  for character in contents.lower():
    characters_dict[character] = characters_dict.get(character, 0) + 1
  return characters_dict



def get_num_words(text):
  words_list = text.split()
  return len(words_list)

def get_char_count(text):
  freq = {}

  for char in text:
    char = char.lower()
    if char not in freq:
      freq[char] = 1
    else:
      freq[char] += 1
  return freq



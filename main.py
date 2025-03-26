import sys
from stats import get_num_words, get_char_count

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def format_report(text, fileName):
  num_words = get_num_words(text)
  char_count = get_char_count(text)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {fileName}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
  for char, count in char_count:
    if char.isalpha():
      print(f"{char}: {count}")
  print("============= END ===============")


if __name__ == "__main__":
  
  sys_list = sys.argv
  if len(sys_list) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
  book_name = sys_list[1]
  print(book_name)
  
  text = get_book_text(book_name)
  format_report(text, book_name)
  


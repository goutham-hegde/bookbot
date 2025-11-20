import sys
from stats import count_words,get_char_count,sort_char,sort_on
def main():
  
  if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  num_words=count_words(sys.argv[1])
  num_char=get_char_count(sys.argv[1])
  l=sort_char(num_char)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for i in l:
    
    if i["char"].isalpha():
      print(f"{i["char"]}: {i["num"]}")
  print("============= END ===============")  
main()
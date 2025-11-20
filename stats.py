def get_books_text(filepath):
  with open(filepath) as f:
    file_contents=f.read()
  return file_contents
def count_words(filepath):
  with open(filepath) as f:
    file_contents=f.read()
    word_cnt=file_contents.split()
  return len(word_cnt)
def get_char_count(filepath):
  d={}
  with open(filepath) as f:
    file_contents=f.read()
    for i in file_contents:
      if i.lower() in d:
        d[i.lower()]+=1
      else:
        d[i.lower()]=1
  return d
def sort_char(d):
  l=[]
  for i in d:
    temp_dict={}
    temp_dict["char"]=i
    temp_dict["num"]=d[i]
    l.append(temp_dict)

  l.sort(reverse=True, key=sort_on)
  return l
def sort_on(items):
  return items["num"]
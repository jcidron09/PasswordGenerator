import os

def get_word_by_index(index):
    words = read_words()
    return words[index]

def convert_lines():
  return (" ").join(read_words())

def read_words():
  os.chdir(os.path.curdir + "/Words")
  with open("words_alpha.txt", "r") as file:
      lines= []
      for line in file:
          lines.append(line)
      return lines



if __name__ == "__main__":
    print(get_word_by_index(2))
  

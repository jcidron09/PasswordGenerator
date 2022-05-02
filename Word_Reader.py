import os


os.chdir("/Users/dimicooler/Desktop/Projects/Website/Words")

def get_word_by_index(index):
    return read_words()[index]

def convert_lines():
        return (" ").join(read_words())

def read_words():
    with open("words_alpha.txt") as file:
        lines= []
        for line in file:
            lines.append(line)
        return lines



if __name__ == "__main__":
    print(convert_lines())
    print(read_words()[2])
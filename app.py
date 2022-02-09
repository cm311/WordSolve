
import random
import gui

def open_word_file():
    text = []
    f = open('sgb-words.txt', 'r')
    for line in f:
        text.append(line)
    return text

def select_word(most_common, word_bank):
    return word_bank[random.randint(0, most_common)]

def main():
    word_bank = open_word_file()
    correct_word = select_word(1000, word_bank)
    print(correct_word)

if __name__ == "__main__":
    main()
    app = gui.Application()
    app.master.title('Sample app')
    app.master.minsize(800, 600) 
    app.mainloop()

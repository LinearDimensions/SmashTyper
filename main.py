import keyboard
import utils
import os

class WordBuilder():
    def __init__(self):
        self.data_dict = utils.load_dict()
        self.word = []
        self.sentence = []
        self.count = 0
    def cfm_word(self):
        self.sentence.append(self.word)
        self.word = []
        self.count = 0
    def next_word(self):
        if self.count + 1 >= len(self.get_word()):
            self.count = 0
        else:
            self.count += 1
    def del_word(self):
        self.count = 0
        self.word = []
    def backspace(self):
        if len(self.word) != 0:
            keyboard.send('ctrl+backspace')
    def end_sentence(self):
        pass
    def add_char(self,char):
        self.count = 0
        self.word.append(char)
    def get_word(self):
        return utils.posStr(self.word,self.data_dict)

def callback(event):
    if event.event_type == 'up':
        if event.name == 'space':
            word.cfm_word()
            keyboard.write(' ')
        elif event.name == 'ctrl':
            word.backspace()
            word.next_word()
            keyboard.write(word.get_word()[word.count])
        elif event.name == 'backspace':
            keyboard.send('ctrl+backspace')
            word.del_word()
        elif len(event.name) == 1:
            word.backspace()
            word.add_char(event.name)
            keyboard.write(word.get_word()[word.count])
        elif event.name == 'esc':
            return None

word = WordBuilder()
keyboard.hook(callback, suppress=True,on_remove=True)
print("SmashTyper Activated ...")
input()
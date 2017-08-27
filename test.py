from tkinter import *
from tkinter import ttk

class App:
    def __init__(self):
        self.shouldStartFromBeginning = True
        self.setUpRoot ()
        self.setUpLabel ()
        self.setUpButtons ()
        self.root.mainloop ()

    def keyPress (self, event):
        self.onButtonClicked(event.char)

    def setUpRoot (self):
        self.root = Tk ()
        self.root.resizable (True, True)
        self.root.bind ('<KeyPress>', self.keyPress)
        self.root.bind('')
    
    def setUpLabel (self):
        self.label = Canvas (self.root, height = 200, width = 190)
        self.scrolly = Scrollbar (self.root, orient = 'vertical', command = self.label.yview)
        self.label.config (scrollregion = self.label.bbox('all'), yscrollcommand = self.scrolly.set)
        self.label.pack(fill='both', expand=True, side='top')
        self.scrolly.pack(fill='y', side='right')
        #self.label.config (aspect = 110, pady = 20,padx = 20, font = 'ariel')

    def onButtonClicked (self, which):
        if which in VALID_NUMBERS:
            if self.shouldStartFromBeginning:
                self.label.config(text = "")
                self.shouldStartFromBeginning = False
            self.label.config(text = self.label['text'] + which + '')
        if which in VALID_OPERATORS:
            self.label.config(text = self.label['text'] + which + '')
            self.VALID_OPERATORS()
            if which in ['/', '*', '+', '-']:
                self.shouldStartFromBeginning = False
            else:
                self.shouldStartFromBeginning = True
        if which == '\x08':
            self.remove()
        if which == '\r':
            self.equal()
            self.shouldStartFromBeginning = True
            

    def createButton (self, text, position):
        return ttk.Button(self.label, text = text, command = lambda : self.onButtonClicked(text)).pack(side = position)

    def setUpButtons (self):
        self.buttons = {
            'zero': self.createButton('0', 'left'),
            'one': self.createButton('1', (5, 0)),
            'two': self.createButton('2', (5, 1)),
            'three': self.createButton('3', (5, 2)),
            'four': self.createButton('4', (4, 0)),
            'five': self.createButton('5', (4, 1)),
            'six': self.createButton('6', (4, 2)),
            'seven': self.createButton(str(7), (3, 0)),
            'eight': self.createButton('8', (3, 1)),
            'nine': self.createButton('9', (3, 2)),
            'ten': self.createButton('/', (2, 3)),
            'multiply': self.createButton('*', (3, 3)),
            'plus': self.createButton('+', (5, 3)),
            'minutes': self.createButton('-', (4, 3)),
            'equals': self.createButton('=', 'right'),
            'dot': self.createButton('.', 'left'),
            'remove': self.createButton('C', 'right'),
            'clear': self.createButton('CE', (2, 0)),
            'power': self.createButton('x2', (2, 2)),
            'radical': self.createButton('√', (2, 1))
        }
        return self.buttons

    def VALID_OPERATORS(self):
        if '=' in self.label['text']:
            self.shouldStartFromBeginning = True
            self.equal()
        if 'CE' in self.label['text']:
            self.clearAll()
        if 'x2' in self.label['text']:
            self.pow()
        if '√' in self.label['text']:
            self.sqrt()
        if 'C' in self.label['text']:
            self.remove()


    def equal(self):
        self.withOutEqual = self.replace('=')
        self.label['text'] = str(eval(self.withOutEqual))

    def clearAll(self):
        self.label['text'] = self.replace(self.label['text'])

    def pow(self):
        self.label['text'] = self.replace('x2')
        self.label['text'] = str(math.pow(int(self.label['text']), 2))

    def sqrt(self):
        self.label['text'] = self.replace('√')
        self.label['text'] = str(math.sqrt(int(self.label['text'])))

    def remove(self):
        self.label['text'] = self.replace('C')
        self.label['text'] = self.label['text'][:len(self.label['text']) - 1]
        print(self.label['text'][:len(self.label['text']) - 2])

    def replace(self, char):
        self.label['text'] = self.label['text'].replace(char, '')
        return self.label['text']

app = App()
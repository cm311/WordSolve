import tkinter as tk

def show_qwerty(parent_frame):
    letters_frame = tk.Frame(parent_frame, relief=tk.GROOVE, width=160,height=40)

    q = tk.Label(letters_frame, text='Q', bg='#0ff444fff')
    w = tk.Label(letters_frame, text='W', bg='#fff000fff')
    e = tk.Label(letters_frame, text='E', bg='#fff000fff')
    r = tk.Label(letters_frame, text='R', bg='#fff000fff')
    t = tk.Label(letters_frame, text='T', bg='#fff000fff')
    y = tk.Label(letters_frame, text='Y', bg='#fff000fff')
    u = tk.Label(letters_frame, text='U', bg='#fff000fff')
    i = tk.Label(letters_frame, text='I', bg='#fff000fff')
    o = tk.Label(letters_frame, text='O', bg='#fff000fff')
    p = tk.Label(letters_frame, text='P', bg='#fff000fff')

    a = tk.Label(letters_frame, text='A', bg='#fff000fff')
    s = tk.Label(letters_frame, text='S', bg='#fff000fff')
    d = tk.Label(letters_frame, text='D', bg='#fff000fff')
    f = tk.Label(letters_frame, text='F', bg='#fff000fff')
    g = tk.Label(letters_frame, text='G', bg='#fff000fff')
    h = tk.Label(letters_frame, text='H', bg='#fff000fff')
    j = tk.Label(letters_frame, text='J', bg='#fff000fff')
    k = tk.Label(letters_frame, text='K', bg='#fff000fff')
    l = tk.Label(letters_frame, text='L', bg='#fff000fff')

    z = tk.Label(letters_frame, text='Z', bg='#fff000fff')
    x = tk.Label(letters_frame, text='X', bg='#fff000fff')
    c = tk.Label(letters_frame, text='C', bg='#fff000fff')
    v = tk.Label(letters_frame, text='V', bg='#fff000fff')
    b = tk.Label(letters_frame, text='B', bg='#fff000fff')
    n = tk.Label(letters_frame, text='N', bg='#fff000fff')
    m = tk.Label(letters_frame, text='M', bg='#fff000fff')

    row1 = [q, w, e, r, t, y, u, i, o, p]
    row2 = [a, s, d, f, g, h, j, k, l]
    row3 = [z, x, c, v, b, n, m]

    for i, lab in enumerate(row1):
        lab.grid(row=0, column=i)
    for i, lab in enumerate(row2):
        lab.grid(row=1, column=i)
    for i, lab in enumerate(row3):
        lab.grid(row=2, column=i)
    return letters_frame

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(sticky=tk.W)

        self.row1 = tk.Frame(self, width=200, height=20, bg='#00f')
        self.row2 = tk.Frame(self, width=200, height=20)
        self.row3 = tk.Frame(self, width=200, height=20)
        self.row4 = tk.Frame(self, width=200, height=20)
        self.row5 = tk.Frame(self, width=200, height=20)
        self.row6 = tk.Frame(self, width=200, height=20)

        guess_rows = [self.row1, self.row2, self.row3, self.row4, self.row5, self.row6]
        for i, r in enumerate(guess_rows):
            guess_rows[i].grid(row=i, column=0)


        self.letters = show_qwerty(self)
        self.letters.grid(sticky=tk.S)

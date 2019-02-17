#!/usr/bin/python

from Tkinter import *

class App:

    def __init__(self, master):
        
        self.master = master

        self.entries = []
        self.i = 2
        self.entry = self.i - 2
        self.row_num = 1
        self.col_num = 0
        rows = 1
        cols = 0
        size = 5

        while cols < size:
            while rows < size + 1:
                self.entries.append(Entry(master))
                self.entries[self.entry].grid(row=rows, column=cols)
                self.i+=1
                self.entry = self.i - 2
                self.row_num += 1
                rows += 1
            rows = 1
            cols += 1
            self.col_num += 1

        f1 = Frame(self.master)
        self.add_row_button = Button(
            f1, text="+", command=self.add_row
            )

        self.sub_row_button = Button(
            f1, text="-", command=self.sub_row
            )

        f1.grid(row=0, column=0)
        self.add_row_button.pack(side=LEFT)
        self.sub_row_button.pack(side=LEFT)

    def add_row(self):
        
        self.entries.append(Entry(self.master))
        self.i += 1
        self.entries[self.entry].grid(row=self.row_num)
        self.entry = self.i - 2
        self.row_num += 1

    def sub_row(self):
        
        self.entries[self.entry-1].grid_forget()
        self.entries.pop()
        self.i -= 1
        self.entry = self.i - 2
        self.row_num += 1
        
root = Tk()

app = App(root)
root.mainloop()

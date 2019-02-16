#!/usr/bin/python

from Tkinter import *

class App:

    def __init__(self, master):
        
        self.master = master
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="Quit", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(
            frame, text="Hello", command=self.say_hi
            )
        self.hi_there.pack(side=LEFT)

        self.entries = []
        self.i = 0
        while self.i < 10:
            self.entries.append(Entry(master))
            self.entries[self.i].pack(side=LEFT)    
            self.i+=1

        self.add_row_button = Button(
            frame, text="+", command=self.add_row
            )
        self.add_row_button.pack()

        self.sub_row_button = Button(
            frame, text="-", command=self.sub_row
            )
        self.sub_row_button.pack()

    def say_hi(self):

        print "hi there, everyone!"

    def add_row(self):
        
        self.entries.append(Entry(self.master))
        self.i += 1
        self.entries[self.i-1].pack(side=LEFT)

    def sub_row(self):
        
        self.entries[self.i-1].pack_forget()
        self.entries.pop()
        self.i -= 1
        
root = Tk()

app = App(root)
root.mainloop()

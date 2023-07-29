# -*- coding: ISO-8859-1 

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

win = Tk()
win.title('Sudoku Solver')


class WindowCreator:
    def __init__(self, window):
        self.win = window
        self.win.geometry("500x500")
        self.label = Label(self.win, text="Select a Sudoku Board image")
        self.label.config(font=("Courier", 14))
        self.label.grid(row=1, column=3)

    def buttons_creator(self):
        self.b1 = Button(self.win, text="Open file", command=self.get_sudoku_file)
        self.b2 = Button(self.win, text="Solve Sudoku", command=self.win_destroy)

        self.b1.grid(row=3, column=2, pady=10)
        self.b2.grid(row=4, column=2, pady=10)

    def get_sudoku_file(self):
        # create 'open file' option
        self.bp_path = filedialog.askopenfilename(title="Select Sudoku Board image",
                                                  filetypes=(("all files", "*.*"), ("text files", "*.txt")))
        self.bp_str = tkinter.StringVar()
        self.bp_label = tkinter.Label(self.win, textvariable=self.bp_str, fg='red')
        self.bp_label.grid(row=3, column=3)
        self.bp_str.set("")
        if self.bp_path:
            # I put several spaces so that, when opening another file using the same button, the StringVar do not overlap
            # visually
            self.bp_str.set(f"                              {self.bp_path}                                            ")

        self.b2.grid(row=20, column=3)

    def win_destroy(self):
        win.destroy()
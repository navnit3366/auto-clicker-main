# For Python GUI
import tkinter as tk


class Window():
    def __init__(self, master):
        self.master = master

    def HorizontalFrame(self, height=100):
        frame = tk.Frame(master=self.master, height=height)
        frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        return frame

    def Button(self, textVariable, command, pad=20, font='Calibri 15 bold', fg='white', bg='black', side=tk.TOP):
        button = tk.Button(master=self.master, textvariable=textVariable, command=command, font=font, fg=fg, bg=bg, relief='raised')
        button.pack(padx=pad, pady=pad, side=side)
        return button

    def Label(self, text, font='Calibri 15 bold', fg='black', relx=0.5, rely=0.5, anchor=tk.CENTER):
        label = tk.Label(master=self.master, text=text, font=font, fg=fg)
        label.place(relx=relx, rely=rely, anchor=anchor)
        return label

    def Entry(self, font='Calibri 15 bold', width=10, relx=0.5, rely=0.5, anchor=tk.CENTER):
        entry = tk.Entry(master=self.master, font=font, width=width)
        entry.place(relx=relx, rely=rely, anchor=anchor)
        return entry

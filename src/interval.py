# To edit tkinter entries
import tkinter as tk


def returnInt(text):
    text = text.replace(' ', '')
    text = text.replace(',', '')
    if text == '':
        return 0

    try:
        return float(text)
    except:
        return 0


def getInterval(entries):
    hours = returnInt(entries[0].get())
    minutes = returnInt(entries[1].get())
    seconds = returnInt(entries[2].get())
    print(hours, minutes, seconds)
    seconds = float(hours) * 3600 + float(minutes) * 60 + float(seconds)

    if seconds < 0.1:
        print("Interval can't be less than 100 milliseconds")
        entries[2].delete(0, tk.END)
        entries[2].insert(0, '0.1')
        return 0.1

    return float(hours) * 3600 + float(minutes) * 60 + float(seconds)

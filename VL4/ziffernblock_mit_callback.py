# Schaltflächen für die Ziffern von 1 bis 9 sollten
# in einem 3x3 Layout angezeigt werden
import tkinter 
from tkinter import messagebox
import random
from functools import partial

haupt_fenster = tkinter.Tk()
haupt_fenster.title("Ziffernblock")

def sage_zahl(zahl: int):
    messagebox.showinfo("THI", f"Du hast {zahl} gedrückt")

zahl = 1
farben = ["blue", "red", "green", "yellow", "#ff00ff"]
for zeile in range(3):
    for spalte in range(3):
        button = tkinter.Button(haupt_fenster, text=zahl)
        button.config(width=10, height=5)
        button.config(background = random.choice(farben))
        button.config(command = partial(sage_zahl, zahl))
        button.grid(row = zeile, column = spalte)
        zahl += 1 # zahl = zahl + 1

haupt_fenster.mainloop()
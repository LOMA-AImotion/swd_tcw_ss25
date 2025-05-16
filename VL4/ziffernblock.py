# Schaltflächen für die Ziffern von 1 bis 9 sollten
# in einem 3x3 Layout angezeigt werden
import tkinter 
import random
haupt_fenster = tkinter.Tk()
haupt_fenster.title("Ziffernblock")

zahl = 1
farben = ["blue", "red", "green", "yellow", "#ff00ff"]
for zeile in range(3):
    for spalte in range(3):
        button = tkinter.Button(haupt_fenster, text=zahl)
        button.config(width=10, height=5)
        button.config(background = random.choice(farben))
        button.grid(row = zeile, column = spalte)
        zahl += 1 # zahl = zahl + 1

haupt_fenster.mainloop()
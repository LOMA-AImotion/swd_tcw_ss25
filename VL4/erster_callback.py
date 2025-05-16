import tkinter
from tkinter import messagebox
import webbrowser

def sag_servus():
    messagebox.showerror("THI", "Servus WI, Klausur nicht bestanden")
    print("Servus TCW WI-M")
    sag_servus_button.config(background="red")
    textfeld.config(text="Servus geklickt")


def öffne_THI_website():
    webbrowser.open("https://www.thi.de/weiterbildung/campus-fuer-weiterbildung/")
    textfeld.config(text="Website geklickt")

haupt_fenster = tkinter.Tk()
textfeld = tkinter.Label(haupt_fenster, text="Hallo!")
textfeld.pack()

sag_servus_button = tkinter.Button(haupt_fenster, 
                                   text="Sag Servus",
                                   command=sag_servus)
sag_servus_button.pack()
website_button = tkinter.Button(haupt_fenster, text="Öffne Website", command=öffne_THI_website)
website_button.pack()
haupt_fenster.mainloop()
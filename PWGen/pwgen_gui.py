import tkinter
import pwgen_funktionen

haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI TCW - PWGen")
pwgen_button = tkinter.Button(haupt_fenster, text="Generiere Passwort")
pwgen_button.pack()

pw_label = tkinter.Label(haupt_fenster, text="Passwort:")
pw_label.pack()

import os
adjektive_pfad = os.path.join(os.path.dirname(__file__), "adjektive.txt")
nomen_pfad = os.path.join(os.path.dirname(__file__), "nomen.txt")

# generiere ein neues Passwort
# schreib es in das pw_label
def neues_passwort():
    neues_passwort = pwgen_funktionen.generiere_passwort(adjektive_pfad, nomen_pfad)
    pw_label.config(text = f"Passwort:{neues_passwort}")

pwgen_button.config(command = neues_passwort)
haupt_fenster.mainloop()
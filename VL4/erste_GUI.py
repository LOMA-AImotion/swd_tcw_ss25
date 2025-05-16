import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI TCW, SWD SS25")
label = tkinter.Label(haupt_fenster, text="Hallo TCW")
tkinter.Label()
label.pack()

button = tkinter.Button(haupt_fenster, text="OK", background="#ff00ff")
button.pack()

haupt_fenster.mainloop()
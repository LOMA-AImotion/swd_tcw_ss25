import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI TCW, SWD SS25")
leinwand = tkinter.Canvas(haupt_fenster, width=600, height=300, background="yellow")
leinwand.grid(row=0, column=0, rowspan=4, columnspan=2)

label = tkinter.Label(haupt_fenster, text="Hallo TCW")
tkinter.Label()
label.grid(row=0, column=1)

button = tkinter.Button(haupt_fenster, text="OK", background="#ff00ff")
button.grid(row=1, column=0)

haupt_fenster.mainloop()
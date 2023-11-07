from tkinter import *
import webbrowser

def encender():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

root = Tk()
label = Label(root, text = "Hola Mundo")
label.pack()
miboton = Button(root, text = "Mira un botón", command = encender())
miboton.pack()
root.mainloop()
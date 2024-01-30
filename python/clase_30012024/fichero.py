from tkinter import *
# Hold onto a global reference for the root window
root = None

def buttonPushed():
  # abrir el fichero y
  fichero = open("./ejemplo.txt", "r")
  txt.insert (END, fichero.read())
  fichero.close()

def main():
  global root
  global txt
  root = Tk() # Create the root (base) window where all widgets go
  w = Label(root, text="Hello, world!") # Create a label with words
  w.pack() # Put the label into the window
  txt = Text(root, height = 5, width = 52)
  #txt.insert(root.END, "ejemplo")
  txt.pack()
  myButton = Button(root, text="Exit",command=buttonPushed)
  myButton.pack()
  root.mainloop() # Start the event loop

main()
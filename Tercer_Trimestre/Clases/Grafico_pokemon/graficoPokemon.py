import pandas as ps
import matplotlib.pyplot as plt
from tkinter import *

class DataFrame:
    def __init__(self):
        self.dataframe = ps.read_csv("./pokemonDB_dataset.csv", delimiter=",", encoding="utf-8")
        
    def plot(self, pokemon):
        self.dataframe[self.dataframe["Pokemon"] == pokemon].plot(x="Type" , y="HP Base", title=pokemon, kind="bar")
        plt.show()

class Stats(DataFrame):
    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.geometry("815x250")
        self.window.title("Pokemon Stats")
        self.start()
    
    def label(self):
        self.welcome = Label(self.window, text="Welcome to Pokemon Stats\n\
Chose the Pokemon you want to see")
        self.welcome.pack()
    
    def scrollbar(self):
        self.scroll = Scrollbar(self.window, orient="vertical")
        self.scroll.pack(side=RIGHT, fill=Y)
        
    def canvas(self):
        self.canva = Canvas(self.window, bd=0, highlightthickness=0, yscrollcommand=self.scroll.set)
        self.canva.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        self.scroll.config(command=self.canva.yview)
        self.canva.bind('<Configure>', lambda e: self.canva.configure(scrollregion=self.canva.bbox("all")))
        self.frame = Frame(self.canva)
        self.frame_id = self.canva.create_window((0,0), window=self.frame, anchor=NW)
    
    def button(self):
        for i in range(len(self.dataframe)):
            self.pokemon = self.dataframe["Pokemon"][i]
            self.buton = Button(self.frame, text=self.pokemon, command=lambda pokemon=self.pokemon: self.plot(pokemon))
            self.buton.pack(fill=X)
            
    def exit(self):
        self.buton = Button(self.frame, text="Salir", command=self.window.destroy)
        self.buton.pack(fill=X)
        
        
    def start(self):
        self.label()
        self.scrollbar()
        self.canvas()
        self.button()
        self.exit()
        self.window.mainloop()
  
s = Stats()
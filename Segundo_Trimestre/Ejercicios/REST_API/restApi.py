import tkinter as tk
from tkinter import ttk
import requests

class Users:
    
    def __init__(self, userid, id, title, completed):
        self.userid =userid
        self.id = id
        self.title = title
        self.completed = completed
        
    def characteristics(self):
        self.window = tk.Tk()
        self.window.geometry("815x250")
        self.window.title("Adding a Vertical Scrollbar to a Treeview Widget")

        self.tree = ttk.Treeview(self.window, columns=('User ID', 'Proyect ID', 'Title', 'Status'))
        self.head()

    def api():
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        data = response.json()
        return data
    
    def head(self):
        self.tree.heading('User ID', text='User ID')
        self.tree.heading('Proyect ID', text='Proyect ID')
        self.tree.heading('Title', text='Title')
        self.tree.heading('Status', text='Status')
        self.tree.column('#0', width=0)
        
    def insert(self):
        self.tree.insert('', 'end', values = (self.userid, self.id, self.title, self.completed))
        
    def start(self):
        self.tree.pack()
        self.window.mainloop()

u = Users(None, None, None, None)
u.characteristics()

for user in Users.api():
    u.__init__(user["userId"], user["id"], user["title"], user["completed"])
    u.insert()
    
u.start()
    


'''
Esta es otra manera

class Usuairo:
    
    def __init__(self, userid, id, title, completed):
        self.userid = userid
        self.id = id
        self.title = title
        self.completed = completed
        
    def mostrarContenido(self):
        return f'El id del usuario: {self.userid}, El id del proyecto: {self.id}, EL titulo del proyecto: {self.title}, El estado del proyecto: {self.completed}'

response = requests.get("https://jsonplaceholder.typicode.com/todos/")
data = response.json()  # Convert the response to JSON

for user in data:
    u = Usuairo(user["userId"], user["id"], user["title"], user["completed"])
    print(u.mostrarContenido())'''
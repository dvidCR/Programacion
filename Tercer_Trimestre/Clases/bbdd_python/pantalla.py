from tkinter import ttk
import tkinter as tk
from dispatcher import dispatcher


# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("400x280") 
my_w.title("ejemplo")  
# Using treeview widget
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=1,column=1,padx=20,pady=20)

# number of columns
trv["columns"] = ("1", "2", "3","4","5")

# Defining heading
trv['show'] = 'headings'

# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')

# Headings  
# respective columns
trv.heading("1", text ="id")
trv.heading("2", text ="Name")
trv.heading("3", text ="Apellido")
trv.heading("4", text ="Edad")  

# Dispatcher
d = dispatcher()
d.cargarAgenda()
id = 1
for contacto in d.getAgenda().getAgenda():
    trv.insert("", 'end', iid=id, text=id, values=(
        id, contacto.getNombre(), contacto.getApellido(), contacto.getEdad()))
    id+=1

# getting data from MySQL student table 
my_w.mainloop()
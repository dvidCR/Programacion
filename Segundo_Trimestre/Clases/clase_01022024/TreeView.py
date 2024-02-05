import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Adding a Vertical Scrollbar to a Treeview Widget")

# create a treeview
tree = ttk.Treeview(window, columns=('archivo', 'modificado', 'último acceso', 'tamaño (Kb)'))

# define the columns
tree.heading('archivo', text='archivo')
tree.heading('modificado', text='modificado')
tree.heading('último acceso', text='último acceso')
tree.heading('tamaño (Kb)', text='tamaño (Kb)')
tree.column('#0', width=0)

formato = '%d-%m-%y %H:%M:%S'
ruta_app = os.getcwd()
contenido = os.listdir(ruta_app)
archivos = 0
total = 0
linea = '-' * 40

# add some data to the treeview
for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    #if not os.access(archivo, os.R_OK) and os.path.isfile(archivo):
    estado = os.stat(archivo)  # obtiene estado del archivo
    tamaño = estado.st_size  # obtiene de estado el tamaño 
    
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime. 
    
    ult_acceso = datetime.fromtimestamp(estado.st_atime)
    modificado = datetime.fromtimestamp(estado.st_mtime)
    
    # Se aplica el formato establecido de fecha y hora
    
    ult_acceso = ult_acceso.strftime(formato)
    modificado = modificado.strftime(formato)
    
    # Se acumulan tamaños y se muestra info de cada archivo
    
    total += tamaño
    tree.insert('', 'end', values = (elemento, modificado, ult_acceso,round(tamaño/1024, 1)))

# pack the treeview
tree.pack()

# start the main loop
window.mainloop()
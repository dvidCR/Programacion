import sys
from bbdd import BBDD
import subprocess
try:
    import PySimpleGUI as sg
except:
    subprocess.check_call(["pip", "install", "PySimpleGUI==4.27.4"])
    import PySimpleGUI as sg

class UI(BBDD):
    
    def __init__(self):
        self.root = sg
        try:
            super().__init__(self.usuario, self.password, self.bbdd)
            self.mainButton()
        except:
            self.login()
        
    def mainButton(self):
        button = [  [self.root.Text("Control de Empleados")],
            [self.root.Button('Ver la lista de empleados completa')],
            [self.root.Button('Dar de alta un nuevo empleado')], 
            [self.root.Button('Dar de alta un empleado')],
            [self.root.Button('Dar de baja a un empleado')],
            [self.root.Button('Cambiar de puesto a un empleado')],
            [self.root.Button('Cambiar el número de un empleado')],
            [self.root.Button('Salir')] ]
        self.layout(button)
        
    def login(self):
        datos = [  [self.root.Text("Pon el nombre de tus credenciales")],
            [self.root.InputText()], 
            [self.root.Text("Pon la contraseña")],
            [self.root.InputText()],
            [self.root.Button('Enviar'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
    def verTabla(self, datos):
        cabezera = ["ID", "Nombre", "Apellidos", "DNI", "Puesto", "Telefono", "Alta", "Baja"]
        tabla = [   [self.root.Table(values=datos, 
                                     headings=cabezera,
                                     auto_size_columns=True,
                                     display_row_numbers=False,
                                     justification='center',
                                     row_height=35,
                                     num_rows = 8)],
            [self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(tabla)
        
    def nuevoEmpleado(self):
        datos = [  [self.root.Text("Añadir el nombre del empleado")],
            [self.root.InputText()], 
            [self.root.Text("Añadir los apellidos del empleado")],
            [self.root.InputText()],
            [self.root.Text('Añadir el DNI del empleado')],
            [self.root.InputText()],
            [self.root.Text('Añadir el puesto del empleado')],
            [self.root.InputText()],
            [self.root.Text('Añadir el teléfono del empleado')],
            [self.root.InputText()],
            [self.root.Button('Añadir'), self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
        
    def altaEmpleado(self):
        datos = [  [self.root.Text("Añade el nombre del empleado al que le quieres dar de alta")],
            [self.root.InputText()], 
            [self.root.Text("Añade los apellidos del empleado al que le quieres dar de alta")],
            [self.root.InputText()],
            [self.root.Text('Añade el DNI del empleado al que le quieres dar de alta')],
            [self.root.InputText()],
            [self.root.Button('Actualizar'), self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
    def bajaEmpleado(self):
        datos = [  [self.root.Text("Añade el nombre del empleado al que le quieres dar de baja")],
            [self.root.InputText()], 
            [self.root.Text("Añade los apellidos del empleado al que le quieres dar de baja")],
            [self.root.InputText()],
            [self.root.Text('Añade el DNI del empleado al que le quieres dar de baja')],
            [self.root.InputText()],
            [self.root.Button('Actualizar'), self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
    def cambiarPuesto(self):
        datos = [  [self.root.Text("Añade el nombre del empleado")],
            [self.root.InputText()], 
            [self.root.Text("Añade los apellidos del empleado")],
            [self.root.InputText()],
            [self.root.Text('Añade el DNI del empleado')],
            [self.root.InputText()],
            [self.root.Text('Añade su nuevo puesto de trabajo')],
            [self.root.InputText()],
            [self.root.Button('Actualizar'), self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
    def cambiarNumero(self):
        datos = [  [self.root.Text("Añade el nombre del empleado")],
            [self.root.InputText()], 
            [self.root.Text("Añade los apellidos del empleado")],
            [self.root.InputText()],
            [self.root.Text('Añade el DNI del empleado')],
            [self.root.InputText()],
            [self.root.Text('Añade su nuevo número de telefono')],
            [self.root.InputText()],
            [self.root.Button('Actualizar'), self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
        
    def layout(self, layout):
        self.window = self.root.Window('Aplicacion de control de datos y estado de los empleados', layout)
    
    def events(self):
        if self.event == self.root.WIN_CLOSED or self.event == 'Salir':
            self.window.close()
            sys.exit()
        elif self.event == 'Retroceder':
            self.window.close()
            self.layout(self.mainButton())
        elif self.event == 'Enviar':
            self.usuario = self.values[0]
            self.password = self.values[1]
            self.bbdd = "empleados"
            
        self.window.close()
            
        match(self.event):
            case 'Ver la lista de empleados completa':
                self.verTabla(self.ver())
                self.update()
            
            case 'Dar de alta un nuevo empleado':
                self.nuevoEmpleado()
                self.update()
                if self.event == 'Añadir':
                    if not self.nuevos(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4])[0]:
                        self.error(self.nuevos(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4])[1])
                        self.update()
            
            case 'Dar de alta un empleado':
                self.altaEmpleado()
                self.update()
                if self.event == 'Actualizar':
                    if not self.altas_bajas("alta", self.values[0], self.values[1], self.values[2])[0]:
                        self.error(self.altas_bajas("alta", self.values[0], self.values[1], self.values[2])[1])
                        self.update()
            
            case 'Dar de baja a un empleado':
                self.bajaEmpleado()
                self.update()
                if self.event == 'Actualizar':
                    if not self.altas_bajas("baja", self.values[0], self.values[1], self.values[2])[0]:
                        self.error(self.altas_bajas("baja", self.values[0], self.values[1], self.values[2])[1])
                        self.update()
            
            case 'Cambiar de puesto a un empleado':
                self.cambiarPuesto()
                self.update()
                if self.event == 'Actualizar':
                    if not self.updateBBDD("puesto", self.values[0], self.values[1], self.values[2], self.values[3])[0]:
                        self.error(self.updateBBDD("puesto", self.values[0], self.values[1], self.values[2], self.values[3])[1])
                        self.update()
            
            case 'Cambiar el número de un empleado':
                self.cambiarNumero()
                self.update()
                if self.event == 'Actualizar':
                    if not self.updateBBDD("telefono", self.values[0], self.values[1], self.values[2], self.values[3])[0]:
                        self.error(self.updateBBDD("telefono", self.values[0], self.values[1], self.values[2], self.values[3])[1])
                        self.update()
    
    def error(self, error):
        datos = [  [self.root.Text(error)],
            [self.root.Button('Retroceder'), self.root.Button('Salir')] ]
        
        self.layout(datos)
    
    def update(self):
        self.event, self.values = self.window.read()
        self.events()
            
if __name__ == '__main__':
    ce = UI()
    while(True):
        ce.update()
        ce.__init__()
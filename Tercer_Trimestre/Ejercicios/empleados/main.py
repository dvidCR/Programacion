import PySimpleGUI as sg
import sys
from bbdd import BBDD

class UI(BBDD):
    
    def __init__(self, nombre, password, bbdd):
        super().__init__(nombre, password, bbdd)
        self.root = sg
        
        
    def mainButton(self):
        self.button = [  [self.root.Text("Control de Empleados")],
            [self.root.Button('Dar de alta un nuevo empleado')], 
            [self.root.Button('Dar de baja a un empleado')],
            [self.root.Button('Cambiar de puesto a un empleado')],
            [self.root.Button('Cambiar el número de un empleado')],
            [self.root.Button('Salir')] ]
        self.layout(self.button)
        
    def nuevoEmpleado(self):
        self.datos = [  [self.root.Text("Añadir el nombre del empleado")],
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
        
        self.layout(self.datos)
        return self.datos
        
    def layout(self, layout):
        self.window = self.root.Window('Aplicacion de control de datos y estado de los empleados', layout)
    
    def events(self):
        event, values = self.window.read()

        if event == self.root.WIN_CLOSED or event == 'Salir':
            self.window.close()
            
        match(event):
            case 'Dar de alta un nuevo empleado':
                self.nuevoEmpleado()
                self.altas(values[0], values[1], values[2], values[3], values[4])
            
            case 'Dar de baja a un empleado':
                pass
            
            case 'Cambiar de puesto a un empleado':
                pass
            
            case 'Cambiar el número de un empleado':
                pass
            
    def update(self):
        self.mainButton()
        self.events()
        
            
if __name__ == '__main__':
    ce = UI("root", "", "empleados")
    ce.update()
import sys
import os
agenda = {
    "fecha": "",
    "tarea": "",
    "asignatura": "",
    "prioridad": "",
}
listaAgenda = []

def añadirFecha(agenda,fecha):
    agenda["fecha"] = fecha
def añadirTarea(agenda,tarea):
    agenda["tarea"] = tarea
def añadirAsignatura(agenda,asignatura):
    agenda["asignatura"] = asignatura
def añadirPrioridad(agenda,prioridad):
    agenda["prioridad"] = prioridad
def añadirAgenda(fecha,tarea,asignatura,prioridad):
    agenda_copia = agenda.copy()
    añadirFecha(agenda_copia, fecha)
    añadirTarea(agenda_copia, tarea)
    añadirAsignatura(agenda_copia,asignatura)
    añadirPrioridad(agenda_copia, prioridad)
    listaAgenda.append(agenda_copia)
def borrarTarea(tarea):
    for i in listaAgenda:
        if i["tarea"] == tarea:
            listaAgenda.remove(i)
def buscarFecha(fecha):
    for i in listaAgenda:
        if i["fecha"] == fecha:
            print(i)
def buscarTarea(tarea):
    for i in listaAgenda:
        if i["tarea"] == tarea:
            print(i)
def buscarAsignatura(asignatura):
    for i in listaAgenda:
        if i["asignatura"] == asignatura:
            print(i)
def buscarPrioridad(prioridad):
    for i in listaAgenda:
        if i["prioridad"] == prioridad:
            print(i)

if __name__ in "__main__":
    while(True):
        print("<------------------------->")
        print("1.Añadir Agenda:")
        print("2.Borrar Agenda: ")
        print("3.Buscar Agenda: ")
        print("4.Ver Agenda: ")
        print("5.Salir")
        print("<------------------------->")
        menu = input("¿Que opción quieres?: ")
        match menu:
            case "1":
                fecha = input("¿Que fecha quieres poner?: ")
                tarea = input("¿Que tarea quires añadir?: ")
                asignatura = input("¿A que asignatura pertenece?: ")
                prioridad = input("¿Que prioridad tiene?: ")
                añadirAgenda(fecha, tarea, asignatura, prioridad)
                os.system("cls")
            case "2":
                tarea = input("¿Que tarea quieres borrar: ?")
                borrarTarea(tarea)
                os.system("cls")
            case "3":
                os.system("cls")
                print("<------------------------->")
                print("1.Buscar por Fecha:")
                print("2.Buscar por Tarea: ")
                print("3.Buscar por Asignatura: ")
                print("4.Buscar por Prioridad: ")
                print("5.Retroceder: ")
                print("<------------------------->")
                buscar = input("¿Que opción quieres?: ")
                match buscar:
                    case "1":
                        buscarFecha(fecha = input("¿Que fecha quieres buscar?: "))
                        os.system("Pause")
                        os.system("cls")
                    case "2":
                        buscarTarea(tarea = input("¿Que tarea quires buscar?: "))
                        os.system("Pause")
                        os.system("cls")
                    case "3":
                        buscarAsignatura(asignatura = input("¿Que asignatura quires buscar?: "))
                        os.system("Pause")
                        os.system("cls")
                    case "4":
                        buscarPrioridad(prioridad = input("¿Por que porioridad qiueres buscar?: "))
                        os.system("Pause")
                        os.system("cls")
                    case "5":
                        os.system("cls")
            case "4":
                print(listaAgenda)
                os.system("Pause")
                os.system("cls")
            case "5":
                os.system("cls")
                sys.exit()
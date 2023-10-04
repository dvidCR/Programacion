import sys
agenda = {
    "fecha": "",
    "tarea": "",
    "prioridad": "",
}
listaAgenda = []

def añadirFecha(agenda,fecha):
    agenda["fecha"] = fecha
def añadirTarea(agenda,tarea):
    agenda["tarea"] = tarea
def añadirPrioridad(agenda,prioridad):
    agenda["prioridad"] = prioridad
def añadirAgenda(fecha,tarea,prioridad):
    agenda_copia = agenda.copy()
    añadirFecha(fecha)
    añadirTarea(tarea)
    añadirPrioridad(prioridad)
    listaAgenda.append(agenda_copia)
def borrarFecha(listaAgenda,fecha):
    for i in listaAgenda:
        if i["fecha"] == fecha:
            listaAgenda.remove(i)
def borrarTarea(listaAgenda,tarea):
    for i in listaAgenda:
        if i["tarea"] == tarea:
            listaAgenda.remove(i)
def borrarPrioridad(listaAgenda,prioridad):
    for i in listaAgenda:
        if i["prioridad"] == prioridad:
            listaAgenda.remove(i)
def borrarAgenda(fecha,tarea,prioridad):
    borrarFecha(fecha)
    borrarTarea(tarea)
    borrarPrioridad(prioridad)
    agenda.append(listaAgenda)
def buscarFecha(listaAgenda,fecha):
    for i in listaAgenda:
        if i["fecha"] == fecha:
            print(i)
def buscarTarea(listaAgenda,tarea):
    for i in listaAgenda:
        if i["tarea"] == tarea:
            print(i)
def buscarPrioridad(listaAgenda,prioridad):
    for i in listaAgenda:
        if i["prioridad"] == prioridad:
            print(i)

if __name__ in "__main__":
    while(True):
        print("<------------------------->")
        print("1.Añadir Agenda:")
        print("2.Borrar Agenda: ")
        print("3.Buscar Fecha: ")
        print("4.Buscar Tarea: ")
        print("5.Buscar Prioridad: ")
        print("6.Salir")
        print("<------------------------->")
        menu = input("¿Que opción quieres?: ")
        match menu:
            case "1":
                añadirAgenda(fecha = input("¿Que fecha quires poner?: "), tarea = input("¿Que tarea quieres poner?: "), prioridad = input("¿Que prioridad quieres poner?: "))
            case "2":
                borrarAgenda(fecha = input("¿Que fecha quires borrar?: "), tarea = input("¿Que tarea quieres borrar?: "), prioridad = input("¿Que prioridad quieres borrar?: "))
            case "3":
                buscarFecha(fecha = input("¿Que fecha quieres buscar?: "))
            case "4":
                buscarTarea(tarea = input("¿Que tarea quires buscar?: "))
            case "5":
                buscarPrioridad(prioridad = input("¿Por que porioridad qiueres buscar?: "))
            case "6":
                sys.exit()
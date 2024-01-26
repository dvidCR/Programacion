import os
import socket


HOST = "localhost"
PORT =  9999


client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

file_name = "./foto.png"

# pasos :
#1. abrirlo
file = open(file_name, "rb")
#2. ¿Cómo obtener el nombre del fichero que queremo enviar?
client.send(file_name.encode())
#3. ¿Cómo obtener el tamaño del fichero?
size = str(os.stat(file_name).st_size)
client.send(size.encode())
#4. cómoleer el fichero y enviarlo tantas veces como líneas tenga 
data = file.read()
client.sendall (data)
client.send(b"<END>")

#file.close()


client.close()
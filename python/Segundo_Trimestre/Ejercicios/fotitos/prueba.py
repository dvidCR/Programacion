import os

file_name = "./descarga.jpg"

file = open(file_name, "rb")

size = str(os.stat(file_name).st_size)

for i in file.read():
    print(i)
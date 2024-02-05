with open('./fichero.txt', 'r') as f:
    print(f.read())
    
j = open('descarga.jpg', 'r+')
jpgdata = j.read()
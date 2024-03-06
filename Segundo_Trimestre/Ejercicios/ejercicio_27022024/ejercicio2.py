lista3D = [[[1, 2, 3], [4, 5, 6], [4, 5, 6], [1, 2, 3]], [[1, 2, 3], [4, 5, 6], [4, 5, 6], [1, 2, 3]], [[1, 2, 3], [4, 5, 6], [4, 5, 6], [1, 2, 3]]]

for i in range(0, len(lista3D)):
    for j in range(0, len(lista3D[i])):
        for v in range(0, len(lista3D[i][j])):
            print(lista3D[i][j][v])
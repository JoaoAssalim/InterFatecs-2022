c, l = input().split()
c1, l1 = input().split()
matriz = []
for row in range(int(c)):
    linha = []
    for column in range(int(l)):
        linha.append('')
    matriz.append(linha)
    
for a in range(int(l)):
    matriz[0][a] = 0
    
for c in range(1, int(c)):
    matriz[c][-1] = 1

for d in range(int(l)-1):
    matriz[-1][d] = 2

for f in range(1, int(c)):
    matriz[f][0] = 3
    
for y in range(len(matriz)):
    for l in range(len(matriz[y])):
        if matriz[y][l] == '':
            I = matriz[y-1][l]
            II = matriz[y][l-1]
            III = matriz[y-1][l-1]
            matriz[y][l] = I + II + III
    
num = matriz[int(c1)-1][int(l1)-1]
print(num)
n = int(input())
lista_n = []
numeros_falt = []

if n >= 1 and n <= 100:

    for i in range(n):
        num = int(input())
        lista_n.append(num)

    for x in range(1, lista_n[-1]):
        if not x in lista_n:
            numeros_falt.append(x)
    
    if len(numeros_falt) == 0:
        print('bom trabalho')
    else:  
        for numero in numeros_falt:
            print(numero)
    
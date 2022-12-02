pessoas, eventos = list(map(int, input().split()))
contato = []
grupos = pessoas
grupos_seguros = 0
covid = []

for i in range(eventos):
    entrada = input().split()
    if entrada[0] == 'c':
        if len(contato) == 0:
            contato.append([entrada[1], entrada[2]])
            grupos -= 1
        else: 
            for i in range(len(contato)):
                if entrada[1] in contato[i]:
                    grupos -= 1
                    contato.append(entrada[2])
                elif entrada[2] in contato[i]:
                    grupos -= 1
                    contato.append(entrada[1])
                else:
                    contato.append([entrada[1], entrada[2]])
                    grupos -= 1

    elif entrada[0] == 'n':
        print(grupos)
    
    elif entrada[0] == 'ni':
        if len(covid) == 0:
            print(0)
        else:
            print(len(grupos_seguros)-len(covid))
            
    elif entrada[0] == 'ns':
        print(grupos - len(covid))
        
    elif entrada[0] == 'ii':
        if len(covid) == 0:
            print('vazio')
        else:
            for i in covid: print(i, end=' ')
    
    elif entrada[0] == 'p':
        covid.append(entrada[1])
        for i in contato:
            if entrada[1] in i:
                for x in contato[i]:
                    covid.append(x)
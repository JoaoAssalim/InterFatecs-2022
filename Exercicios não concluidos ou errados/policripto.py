alfabeto = 'abcdefghijklmnopqrstuvxyz'
nova_palavra = ''

frase = input()
desc = input()

if len(frase) <= 200 and len(desc) <= 400:
    oper = False
    index_desc = 0
    index_letra = 0

    p = desc.count('+')
    l = desc.count('-')
    p = p + l
    tam = len(frase)

    for i in range(len(frase) + p):
        palavra = frase[index_letra]
        val = desc[index_desc]
        if val == '-':
            oper = False
            index_desc += 1
        elif val == '+':
            oper = True
            index_desc += 1
        else:
            if palavra == 'w':
                nova_palavra += ' '
                index_letra += 1
            
            else:
                index = alfabeto.index(frase[index_letra])
                if oper:
                    ex_ind = index
                    ind = index + int(val)
                    if ind >= 25:
                        if ex_ind < 23:
                            ind -= 26
                        else:
                            ind -= 25
                    nova_palavra += alfabeto[ind]
                else:
                    ind = index - int(val)
                    
                    if ind < 0:
                        ind += 26
                    nova_palavra += alfabeto[ind]
                    
                index_desc += 1
                index_letra += 1
                     
    print(f'{nova_palavra}\n')  
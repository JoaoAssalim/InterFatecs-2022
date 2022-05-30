while True:
    numeros = 0
    letras = 0

    try:
        placa = list(map(int, input().split()))
        nova_placa = ''
        for p in placa:
            nova_placa += chr(p)
        
        for item in nova_placa:
            if item.isdigit():
                numeros += 1
            else:
                letras += 1
        
        if numeros == 3 and letras == 4:
            if nova_placa[0].isalpha() and nova_placa[1].isalpha() and nova_placa[2].isalpha() and nova_placa[3].isdigit() and nova_placa[4].isalpha() and nova_placa[5].isdigit() and nova_placa[6].isdigit():
                print('MERCOSUL')
            else:
                print('ERRO')
        elif numeros == 4 and letras == 3:
            if nova_placa[0].isalpha() and nova_placa[1].isalpha() and nova_placa[2].isalpha() and nova_placa[3].isdigit() and nova_placa[4].isdigit() and nova_placa[5].isdigit() and nova_placa[6].isdigit():
                print('ANTIGA')
            else:
                print('ERRO')
        else:
            print('ERRO')
        
    except EOFError:
        break
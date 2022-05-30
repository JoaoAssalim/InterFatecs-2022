I = float(input())
A = float(input())
T = float(input())

if  I>0 and A>0:
    if I == A:
        print('pode comprar agora')
    else:
        meses = 0
        while I <= A:
            I += I*T/100
            meses += 1
        if meses > 1:
            print(f'possivel em {meses} meses')
        else:
            print(f'possivel em {meses} mes')
        

while True:
    a,b = list(map(int, input().split()))
    if a == b == 0:
        break
    matrix = []
    
    for i in range(a):
        linha = input()
        matrix.append(linha)
    
    nA, nB = list(map(int, input().split()))
    
    difA = int(nA / a)
    difB = int(nB / b)

    for i in matrix:
        linha = ''
        for it in i:
            linha += it * difB
        for y in range(difA):
            print(linha)
        
    print()

"""
3 3
###
#__
###
6 9
5 5
"%*&"
$+#"$
#&',.
!+)##
$!&*#
70 40
5 5
."&&!
+-$*"
!*#",
&('$'
#*)$-
50 35
5 5
)*%%)
$*.%&
+&-,$
(-$#$
+*%!*
25 75
0 0
"""
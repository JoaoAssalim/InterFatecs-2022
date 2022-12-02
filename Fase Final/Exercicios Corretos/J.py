for i in range(int(input())):
    A,B = list(map(int, input().split()))
    if ((A * B) % 2 == 0): print("[:=[primeiro]")
    else: print("[segundo]=:]")
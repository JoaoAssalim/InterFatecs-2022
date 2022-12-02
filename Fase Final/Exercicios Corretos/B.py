N = int(input())
total = 1
for i in range(N-1):
    total = (1/total) + 1
    
print(f'{1/total + 1:.15f}')
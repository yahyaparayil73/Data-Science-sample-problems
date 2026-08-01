a = [23,43,65,78,11,17]
n = len(a)
for i in range(n):
    for j in range(2,a[i]):
        if a[i] % j == 0:
            a[i]  = 0    

print(a)
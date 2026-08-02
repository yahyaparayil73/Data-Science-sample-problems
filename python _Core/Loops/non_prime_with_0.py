a = [4, 7, 10, 3, 8, 5]
n = len(a)
for i in range(n):
    for j in range(2,a[i]):
        if a[i] % j == 0:
            a[i]  = 0    

print(a)




a = [4, 7, 10, 3, 8, 5]
n = len(a)
pos = 0


for i in range(len(a)):
    flag = 0
    for j in range(2,a[i]):
        if a[i] % j == 0:
            flag = 1
            break
    if flag == 0:
        pos+=1   
        a[i-pos] = a[i]
print(a)













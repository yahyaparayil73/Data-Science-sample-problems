a = [4, 2,7, 10, 0,3,1, 8, 5]
n = len(a)
pos = 0


for i in range(len(a)):
    flag = 0
    for j in range(2,a[i]):
        if a[i] % j == 0:
            flag = 1
            break
    if flag == 0:   
        temp = a[pos]
        a[pos] = a[i]
        a[i] = temp
        pos+=1
print(a)













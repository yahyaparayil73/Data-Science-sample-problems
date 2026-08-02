a = [4, 7, 10, 3, 8, 5]
n = len(a)
count = 0


for i in range(len(a)):
    for j in range(2,a[i]):
        flag = 0
        if a[i] % j == 0:
            flag = 1
            break
    if flag == 0:
        count+=1   
        a[i-count] = a[i]
print(a)













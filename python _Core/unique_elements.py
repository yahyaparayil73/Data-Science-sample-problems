arr = [10, 20, 30, 10, 20, 10, 40, 20, 10]
arr2 = []
flag = 0

for i in range(0,len(arr)):
    flag = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            flag = 1
            break
    if flag == 0:
        arr2 = arr[i]

print('unique elements are',arr2)

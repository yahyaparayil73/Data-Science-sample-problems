arr = [23,65,34,87,27,765,34,67,27,84,34,90,10]
n= len(arr)
val = 54
pos = 1
arr = arr + [0]

for i in range(n-1,pos,-1):
    arr[i] = arr[i-1]

arr[pos] = val
print(arr)
    

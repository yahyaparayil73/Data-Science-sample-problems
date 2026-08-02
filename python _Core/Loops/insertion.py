arr = [10,20,30,40,50]
n= len(arr)
val = 54
pos = 1
arr = arr + [0]
# print(arr)
# print(arr[n])

for i in range(n,pos,-1):
    arr[i] = arr[i-1]

arr[pos] = val
print(arr)

    

arr = [10,20,30,40,50,65,34,76,98,60]
n= len(arr)
val = 54
pos = 5
# print(arr)
# print(arr[n])

for i in range(pos,n-1):
    arr[i] = arr[i+1]

arr = arr - arr[n-1]

print(arr)

    

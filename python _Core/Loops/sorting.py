arr = [23,65,34,87,27,765,34,67,27,84,34,90,10]
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[j]> arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)

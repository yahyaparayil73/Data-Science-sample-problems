arr1 = [2,4,7,6,3,8,4,5,8,5,5,2,4]
arr2 = []
# print(arr1)

for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(arr2)


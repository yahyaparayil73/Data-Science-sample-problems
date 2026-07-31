arr = [23,65,34,87,27,765,34,67,27,84,34,90,10]
n = len(arr)
max = 0
for i in arr:
    if i > max:
        max = i
print('the largest is ',max)
max2 = 0

for j in arr:
    if  j > max2 and j  < max:
        max2 = j

print('the second largest number is ',max2)
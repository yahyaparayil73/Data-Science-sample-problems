arr1 = [2,4,7,6,3,8,4,5,8,5,5,2,4]
arr2 = arr1

# print(arr2)

for num1 in arr1:
    count = 0
    for num2 in arr2:
        if num1 == num2:
            count+=1
    print(f'frequency of {num1} is {count} ')

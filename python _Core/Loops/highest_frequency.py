arr = [10, 20, 30, 10, 20, 10, 40, 20, 10]

max_count = 0
max_element = 0

for i in range(len(arr)):

    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Highest Frequency Element :", max_element)
print("Frequency :", max_count)
name = str(input('Enter the string:'))  #yahya parayil
print('The entered string is : ',name)
length = len(name)

target = "A"
count = 0

for i in name:
    if i == target:
        count+=1

print(f'{target} appears {count} times in {name}')
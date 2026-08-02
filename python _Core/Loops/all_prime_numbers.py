n = 7
count = 0
flag = 0

for i in range(2,n+1):
    for j in range (2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(f'{i} is prime')
        count+=1
    else:
        print(f'{i} is not prime')
    flag = 0
print(f'number of prime numbers are {count}')
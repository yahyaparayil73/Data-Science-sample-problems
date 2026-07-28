num = int(input('Enter the number '))
flag = 0
for i in range(2,num//2):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print('prime')
else:
    print('not prime')


num = int(input('Enter the number '))
n = num
sum = 0

while num > 0 :
    temp = num%10
    sum = sum + temp * temp * temp
    num = num // 10

if n == sum :
    print('amstrong')
else :
    print('not amstrong')





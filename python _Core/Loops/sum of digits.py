n = int(input('Enter the number :'))    #234
number =n
sum = 0
while n > 0 :
    temp =  n % 10
    sum += temp
    n //= 10

print(f'sum of th digits of {number} is {sum}')


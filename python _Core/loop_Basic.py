
# n = int(input('enter the limit :'))
# print()
# for i in range(1,n+1):
#     print(i)

count = 0
while True:

    n = int(input('enter the limit :'))
    i =1
    while i < n+1:
        print(i)
        i+=1
    count+=1
    print('count is ',count)
    if count > 5:
        break
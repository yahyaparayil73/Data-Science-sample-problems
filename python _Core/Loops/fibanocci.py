number = 10
a = 0
b = 1
for i in range(0,number+1):
    print(a,end = "")
    a,b = b,a+b
    print()
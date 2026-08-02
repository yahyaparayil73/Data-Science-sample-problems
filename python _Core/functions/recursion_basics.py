def print_numb(num):
    if num ==0:
        return
    print(num)
    print_numb(num-1)
    return num

num = 10
print_numb(num)
print(num)





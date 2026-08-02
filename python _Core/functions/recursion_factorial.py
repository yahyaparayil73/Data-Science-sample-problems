def find_fact(num):
    if num == 1:
        return 1
    fact = num * find_fact(num-1)
    return fact

    

num = 13
print(find_fact(num))

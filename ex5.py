def product(x,y):
    if x==0 or y ==0:
        return 0
    else:
        return (product(x,y-1))+x

print(product(5,2)) # 10
print(product(9,3)) # 27

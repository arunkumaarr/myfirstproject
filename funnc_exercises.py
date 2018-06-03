def two_num(x,y):
    if (x%2==0) and (y%2==0):
        # if even return smallest
        return (min(x, y))
        # else return greatest
    elif (x%2!=0) or (y%2!=0):
        return (max(x, y))

a=10
b=20
result=two_num(a,b)
print(result)
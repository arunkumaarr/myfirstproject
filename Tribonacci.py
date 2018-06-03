def tribonacci(x,y):
    for i in range(0,y-3):
        new = (x[i]+x[i+1]+x[i+2])
        print(new)
        x.append(new)

    print(x)

x=[0,1,1]
y=10
tribonacci(x,y)
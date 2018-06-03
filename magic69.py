def magic69(test):
    flag='OFF'
    sum1=0
    for i in test:
        if (i!=6) and flag=='OFF':
            sum1 += i
        elif (i==6):
            flag='ON'
            continue
        elif (i==9) and flag=='ON':
            flag='OFF'
            continue
        elif (i==9) and flag !='ON':
            sum1 += i
    return (sum1)

del1=[9,2,3,4,33,6,2,4,5,9,1,3]
x=magic69(del1)
print(x)

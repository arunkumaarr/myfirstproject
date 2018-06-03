def addtn(array):
    f = 0
    s = 0
    print (array)
    for i in array:
        if i != 6 and f == 0:
            s+=i
        else:
            f=1
            if(i==9):
                f=0

    return s


x = addtn([1,2,3,4,5,6,7,8,9,10]);
print (x)
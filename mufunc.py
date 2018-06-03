def myfunc(str_1):
    mylist = []
    for i in str_1:
        if i%2 or i / 2 == 0:
            mylist[i] = str_1[i].upper
        else:
            mylisy[i] = str_1[i].lower
    print(mylist)

str1="arunkumar"
out=myfunc(str1)
def capitalise(string):
    end= len(string)
    print(end)
    i=0
    mylist=[]
    while i<end:
        if i==0 or i==3:
            mylist.append(string[i].upper())
        else:
            mylist.append(string[i])

        i = i+1

    return ''.join(mylist)

x=capitalise('macdonald')

print(x)
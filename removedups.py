def matches(list1,list2):
    match=[]
    unmatch=[]
    unmatch1=[]
    for i in list1:
        if i in list2:
            match.append(i)
        else:
            unmatch.append(i)

    for z in list2:
        if z in list1:
            continue
        else:
            unmatch1.append(z)
    return (match,unmatch,unmatch1)

x=[1,2,3,4,5,6,7]
y=[3,4,5,55,66,33,12,8,12]

matched,unmatch1,unmatch2=matches(x,y)
print('present in both the list:{}'.format(matched))
print('present in x not in y:{}'.format(unmatch1))
print('present in y not in x:{}'.format(unmatch2))

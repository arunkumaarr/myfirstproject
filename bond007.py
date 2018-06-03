def matchbond(list1):
    match=[0,0,7]
    for i in range(0,len(list1)-2):
        if match==[list1[i],list1[i+1],list1[i+2]]:
            print('Bond is present')
        else:
            print('Bond is not pressent')

x=[1,2,3,4,5,0,0,7,8,5,0,7,0,7]
matchbond(x)
def master_yoda(text):
    list_2=[]
    list_1=text.split( )
    j=-1
    for i in range(0,len(list_1)):
        list_2.append(list_1[j])
        j=j-1

    return (' '.join(list_2))

x='i am home'
new_list=master_yoda(x)
print(new_list)
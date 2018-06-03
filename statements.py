mylist=[]
for x in range(0,50):
    mylist.append(x)

print(mylist)

new_list=[x for x in mylist if x%3==0]
print(new_list)


comp_list = [x for x in range(0,51) if x%3==0]
print(comp_list)

if new_list == comp_list:
    print('True')
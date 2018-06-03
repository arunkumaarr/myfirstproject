a = 5
b = 8
c = 2

if a>b:
    if  a>c:
        print('A is greatest of the three')
    else:
        if b>c:
            print('B is greatest of the three')
else:
    if b>c:
        print('B is greatest of the three')
    else:
        print('C is greatest of the three')

#this is a program to count number of odd and even num in a list

even_count = 0
odd_count = 0
mylist = [1,2,3,44,66,77,23,45,76,98,43,112,121,865]
list_even=[]
list_odd=[]
total = len(mylist)
for num in mylist:
    if num%2 == 0:
        even_count += 1
        list_even.append(num)
    else:
        odd_count += 1
        list_odd.append(num)

print('of the %d items  in mylist \n %d are even \n %d are odd' %(total,even_count,odd_count))
print(list_even)
print(list_odd)

# this code to execute for loop on dictionaries

my_dic = {'k1':1,'k2':2,'k3':3}

for key in my_dic.items():
    print(key)
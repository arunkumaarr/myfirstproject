def splicer(string):
    print(len(string))
    if len(string)%2 == 0:
        return ('Even')
    else:
        return (string[0])

list1=['Arun','chandra','thanu','teja']
x=splicer(list1)
print(x)

print('mP TEST')

mp1=list(map(splicer,list1))
print(mp1)
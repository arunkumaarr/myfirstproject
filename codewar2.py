import string

def disemvowel(string):
    newstr=[]
    x=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
         if i in x:
            continue
         else:
             newstr.append(i)

    string= ''.join(newstr)
    return string


d=disemvowel('This website is for losers LOL!')
print(d)

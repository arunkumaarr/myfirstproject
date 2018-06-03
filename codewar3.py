def longest(s1, s2):
    s1 += s2
    x=set(s1)
    s1=list(x)
    s1.sort()
    #s1.remove()
    return s1


k=longest("aretheyhere", "yestheyarehere")
print(k)
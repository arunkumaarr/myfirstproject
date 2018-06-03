def pig_latin(word):
    if word[0] in 'aeiou':
        print('in if')
        new_word = word +'ay'
        return (new_word)
    else:
        print('in else')
        new_word = word[1::]+word[0]+'ay'
        return (new_word)


x = pig_latin('abirami')
print(x)
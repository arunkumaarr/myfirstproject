def animal_crackers(text):
    word=text.split( )
    print(word)
    for i in word:
        if (i[0][0] == i[1][0]):
            return True
        else:
            return False

string = 'levalheaded llama'
animal_crackers(string)
#working of break continue and pass
name = 'Arun Kumar'

for letter in name:
    #sampe function to br filled up later but do not want the program to interupt
    pass

print('continue in play')

for letter in name:
    if letter == 'n':
        continue
    print(letter)

print('break in play')

for letter in name:
    if letter == 'n':
        break
    print(letter)
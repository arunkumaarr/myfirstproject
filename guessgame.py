from random import randint
num = randint(1, 10)
print("Hey i am thinking of a number bet 1 to 10 can you guess :P")
print('your are left with three chances !!!!')

i=3

while i > 0:
    i -=1
    user_guess1 = int(input('Enter your number Guess1'))
    if user_guess1== num:
        print('you guessed it right')
        break
    else:
        print('Suit up you !!! :)you are left with %d more tries' %(i))
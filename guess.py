import random

# Generate random number from 1 to 100
x = random.randint(1, 101)

while True:
    print('Press q to quit')
    guess = input('Guess a number from 1 to 100: ')
    if guess == 'q':
        print('Number was {}'.format(x))
        break
    if int(guess) == x:
        print('You won!')
        break
    elif int(guess) > x:
        print('Too big')
    else:
        print('Too small')



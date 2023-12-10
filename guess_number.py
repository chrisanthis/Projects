import random
import math

lower = int(input('Enter lower bound:-'))
upper = int(input('Enter upper bound:-'))
chances = round(math.log(upper - lower + 1, 2))
x = random.randint(lower, upper)

count = 0
print(f' You have {chances} to guess the integer!!')
while count<chances:
    count+=1
    guess = int(input('Guess the number:'))
    if guess==x:
        print('You Won!!! Your guess is correct!!')
        print(f'You guess it in {count} tries!')
        break
    elif x>guess:
        print('Your guess too small')
    elif x<guess:
        print('Your guess too high')

if count>chances:
    print(f'The correct number is {x}')
    print('\nBetter luck next time!!')           


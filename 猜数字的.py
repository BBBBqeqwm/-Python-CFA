import random

print('Guees the number')
x=random.randint(1,100)
g=None
while x !=g:
    g= int(input('pic a number between 1 to 100     :'))
    if x ==g:
        print('you guessed')
    elif x > g:
         print('try a bigger number')
    elif x < g:
         print('try a smaller number') 
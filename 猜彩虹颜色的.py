import random

def main():
   """Start a colour guessing game"""
   print("guess the colour")  

   rainbow= [
      "red","orange","yellow",'green','blue','indigo','violet'
      ]
   x= random.choice(rainbow)
   print(x)
   guess = None
   while x != guess:
      guess = str(input('what colour am i thining of?'))
      if x==guess:
        print("you guessed,{}.congratulations you got it right!".format(guess))
        break
      else:
         print('you guessed,{}.Unfortunately its wrong.try again'.format(guess))
main()         
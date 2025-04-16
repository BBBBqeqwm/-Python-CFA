import random
import time
def ta_as():
  words=['elephant','giraffe','chocolate','butterflt','adventure']
  word=random.choise(words)
  print('Welcome to Typing Speed Test')
  print('Type the followoing word as fast as you can:\n\n',word)
  input('press enter to start...')
  st=time.t()
  ui=input('type here')
  et=time.t()
  if ui==word:
    tt=round(et - st,2)
    print(f'Great job, you took {tt}second.')
  else: 
    print(f'incorrect, the correct word is {word}')
if __name__=="__main__":
  ta_as()
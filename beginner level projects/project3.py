#a number guessing game the program will generate a random numbr and the user will guess the no.
# if the number matches it will print something otherwise not
#import random
random_number=5
count=0
c=1
# one can also add some dramatic effect using time module
import time
# instead of taking random no. we can also take a speccific no. then check wit that
while c==1:
  print(" enter the guessed number ")
  guess_number=int(input())
  time.sleep(7)
  #random_number=random.randint(1,100)
  if random_number==guess_number:
    print(f" hey u guessed correctly in {count} attempt ")
    print(f" hey the random number = {random_number}")
  else:
    count+=1
    print(" u didn't get the right number ")
    #print(f"  the random number = {random_number}")
  print("press 2 to stop guessing number ") 
  c=int(input())
      
    

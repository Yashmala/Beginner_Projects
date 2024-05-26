#fortune cookies
""" this is actually a project which shows fortune by giving any random number from the list 
in this we would be importing a module in order to throw random numbers and thus print the fortune according 
to the numbers we can also modify it """
#this is the module which imports randomness
import random
#this is the function which is associated with random value when we want to get integer value as random then we
# wehave to use randint because bydefault it is in float,thus when we want to get float value we can simply
#pass random.random    
print(" project 1 ")     
var2=random.randint(1,10)    
print(var2)
#here we have two ways of doing it firstly set the fortune according to the numbers by if else
#or  by specifying a sequence datatype that stores all the fortunes in text format and then printing it in random manner
#so we will do both approaches
var3=random.randint(1,5)
if var3==1:
    print(f" lucky number = {var2}")
    print(" you would be having a great day")
if var3==2:
    print(f" lucky number = {var2}")
    print(" you will get a good news today")
if var3==3:
    print(f" lucky number = {var2}")
    print(" you will get a oppportunity to meet narendra modi")
if var3==4:
    print(f" lucky number = {var2}")
    print(" be alert, there is danger approaching ")
if var3==5:
    print(f" lucky number = {var2}")
    print(" u will meet ur life partner today")   
 
    #or another way
list2=["you would be having a great day"," u will meet ur life partner today","you will get a good news today"," be alert, there is danger approaching "," you will get a oppportunity to meet narendra modi"]  
print(f" hey your lucky number is {var2} ")
print(random.choice(list2))
print(random.random())



print("project 2")
#magic 8 ball which prints yes ,no or maybe each time u ask it
var1=random.randint(1,10)
print(var1)
if 1<=var1<9:
  list1=['yes','no',"maybe"]#the choice function will give any element from the any non_empty sequence
  print(random.choice(list1))
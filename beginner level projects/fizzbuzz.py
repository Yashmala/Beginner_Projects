i=1

for i in range(101):
   if i%15==0:
      print(" fizzbuzz")
   elif i%5==0:
      print(" buzz ")
   elif i%3==0:
      print(" fizz ")
   else:
      print(i)
        # simplifying the complex

l1=[" fizzbuzz " if i%15==0 else "buzz" if i%5==0 else " fizz "if i%3==0 else i for i in range(101) ]
print(l1)
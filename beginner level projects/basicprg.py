# calci
print(" enter two numbers ")
n1=int(input())
n2=int(input())
print( n1,n2 )

print(" enter the operations to be performed ")
print("1 for addition ")
print("2 for subtraction ")
print("3 for multipication ")
print("4 for division ")
ch=int(input())
if ch == 1:
    print(  (n1+n2) )
elif ch == 2:
    print( (n1-n2))
elif ch == 3:
    print( (n1*n2))
elif ch == 4:
    print( (n1/n2))   
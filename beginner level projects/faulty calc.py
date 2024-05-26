# the program should take two numbers as input and if the numbers are following in case of addition,mutipication and division then it should would give 
#following result
#45*3=555 56+4=77 ,56/6=4
# if other than these numbers are there it should give correct results
li={(45,3),(56,4),(56,6)}
while 1:
    print(" enter two numbers  ")
    n1=int(input())
    n2=int(input())
    print(" enter operations to be performed ")
    in1=input()
    if  n1 and n2 in li:
        if in1 =='+':
            print(77)
        elif in1=='/':
            print(4)
        elif in1=='*':
            print(555)
        else:
            print(n1-n2)
    else:
        if in1 =='+':
           print(n1+n2)
        elif in1=='/':
           print(n1/n2)
        elif in1=='*':
           print(n1*n2)
        else:
           print(n1-n2)
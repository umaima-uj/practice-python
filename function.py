def g_mean (a,b):
    mean =(a*b)/2
    print (f"The mean of {a} and {b} is: {mean}")
    
def is_greater (a,b):
    if(a>b):
        print(f"{a} is greater than {b}")
    elif(a<b):       
        print( f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")   

a = int(input("Enter first number: "))      
b = int(input("Enter second number: "))
g_mean(a,b)
is_greater (a=a,b=b)

c =int(input("Enter third number:"))
d =int(input("Enter forth number:"))
g_mean(c,d)
is_greater (a=c,b=d)
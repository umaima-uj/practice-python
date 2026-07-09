print ("1  addition")
print ("2  subtraction")
print ("3 multiplication")
print ("4  division")
operation = int(input("please select an operation:"))
if(operation in [1,2,3,4]):
     num1 = float(input("choose first number:"))
     num2 = float(input("choose second number:"))

     if (operation ==1):
         result = num1 + num2  
     elif (operation ==2):
         result =num1 -num2
     elif (operation ==3):
         result = num1 * num2
     elif (operation ==4):
         result =num1/num2
         
     else:
         print("invalid operation")
         
     print("the result of operation is {}:" .format(result))
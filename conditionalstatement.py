num = int(input("enter a number"))
if (num%2==0):
   print(num, end =" ")
   print("is a even number")
elif (num%3==0):
    print(num, end =" ")
    print("is a multiple of 3")

else:
    print("number is not valid")
if   int(input("Enter a number")):
    print("Debasish loves pallabi")
    print("Debasish loves Shreya too")
print("Debasish is a loyal person ")
x = int(input("enter a number"))
s =('Sayantan'if (x==5)else
    'Banerjee'if (x==7)else
    'Diya' if (x==8) else
    'priyanka'
)
print(s) 
#maximum of 3 elements
a,b,c = map( int, input("enter three numbers:").split(','))  
if a>b:
    if a>c: print(c,"is maximum element")   
    else: print(c,"is maximum element")  
else:
    if b>c: print(b,'is maximum element')
    else: print(c,'is maximum element')
A = 5<7 or 7>5
print(A)
    


    
    
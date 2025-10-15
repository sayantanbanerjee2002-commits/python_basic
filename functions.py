# create a function that wheather a num is even or odd
# def evenodd(num):
#     if (num%2 == 0):
        
#         print(num,"is an even number")
#     else:
#         print(num,"is an odd number")
# evenodd(int(input('enter a number')))
# def myfun(x,y):
#        print('X :',x)
#        print('Y :',y)
# myfun(45,56)
# def student(name,age):
#     print(f"Name :{name}, Age :{age}")
# student(name =input("Enetr a name"),age =int(input("Enter age")))
#multiply function
# def multiply(*args):
#     res = 1
#     for num in args:
#         res = res*num
#     return res
# numbers =[int(x) for x in input("enetr five numbers").split(" ")]
# print(multiply(*numbers))
# def student_info(*args,**kwargs):
#     print("Subject :",args)
#     print("Details :",kwargs)
# student_info('Mathematics','science','english',name ='Sayantan',age ='23',city ='Kolkata')

# def fun1(x):
#     x[1] = 30
#     for i in range(5):
#         x.append(i)

# my_list = []
# fun1(my_list)
# print(my_list)

# lambda function
# num = lambda x: 'Even' if (x%2 == 0) else 'Odd'
# print(num(int(input("Enter a number"))))
# result = lambda x: "positive" if x>0 else "Negative" if x<0 else "Zero"
# Result = result(int(input("Enter a number")))
# print(Result)
# lamda functtion with list comprerhension
# lis = [lambda x =i: x*10 for i in range(7)]
# result = lis
# for j in result:
#     print(j())
    
# decorator function
# def sum_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"sum of three numbers:{args}")
#         Result = func(*args, **kwargs)
#         return Result
#     return wrapper

# @sum_decorator # add = sum_decorator(add)
# def add(a,b,c):
#     return a+b+c
# print(add(78,45,34))

#factorial decorator
# def factorial_decorator(func):
#     def wrapper(x):
#         Result = func(x)
#         print(f"factorial of {x} is {Result}")
#         return Result
#     return wrapper

# def fact(x):
#     if x == 0 or x == 1:
        
#      return 1
#     else:
#         return x *fact(x-1)
# fact = factorial_decorator(fact)
# print(fact(5))
def fibbonacci_decorator(func):
    def wrapper(x):
        result = func(x)
        print(f"fibbonacci of {x} is {result}")
        return result
    return wrapper

def fibbonacci_helper(x):
    if x <=0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibbonacci_helper(x-1) + fibbonacci_helper(x-2)
@fibbonacci_decorator
def fibbonacci(x):
    return fibbonacci_helper(x)
fibbonacci(int(input('Enter a number')))
    

        

        
    
        








 
    


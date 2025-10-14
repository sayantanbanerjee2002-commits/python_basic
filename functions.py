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

def fun1(x):
    x[1] = 30
    for i in range(5):
        x.append(i)

my_list = []
fun1(my_list)
print(my_list)





 
    


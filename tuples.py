# crete tuples using list
my_list =[ 2,3,5,6]
A = tuple(my_list)
print(A)
# creting tuples with nestled tuples
s1 = (3,5,6,7)
s2 =(10,12,45,56)
my_tuple =(s1, s2)
print(my_tuple)
# creating a tuple with repeatation
my_tuple =("Sayantan")*5
print(my_tuple)
#Acessing elements of Tuples
Students =('Sayantan',22,'CSE')
print(Students[0])
A ='I am a boy'
my_tuple =tuple(A)
print(A[1:4])
#Tuple unpacking
Student =('Deep',23,'Web_developer')
name, age, role = Student
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Role:{role}")
#formatting of string
a, b, c,*_ =('iphone',60,000,'ios')#unpacking of list
print(f"phone_name:{a}")
print(f"cost:{b}")
print(f"operating_system:{c}")
#swapping of the variable with unpacking
a,b =(25,34)
a,b =b,a# swapping of two values
print(a)
print(b)
#example of tuple unpackinf and format string
Student =('Sayantan', 95,85,86)
Student_name, math_score, english_score, science_score =Student
print(f"{Student_name} scored")
print(f"Math:{math_score}")
print(f"English:{english_score}")
print(f"Science:{science_score}")
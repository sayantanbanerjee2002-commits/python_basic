# #creating a Dictionary
# student ={'name':'Deep','age':23,'gender':'male'}
# print(student)
# #adding key in dictionary
# student['grade'] ='A++'
# student['subject'] =('mathematics','physics','english')
# print("update student_details")
# print(student)
#dictionary comprehension

# variable =dict.fromkeys(range(7),[1,3,5,6,7,9,11])
# print(variable)

















# #removing items from dictionary
# d1 ={1:'ram',2:'is',3:'a',4:'boy'}
# del d1[3]
# print(d1)
# D =d1
# value =D.pop(1)
# print(value)
# key,value =D.popitem()
# print(f"Key:{key}, Value:{value}")
# #iteratios over Dictionary
# D ={1:'ram',2:'is',3:'a',4:'boy'}
# for key in D:
#     print(key)
# for value in D.values():
#   print(value) 
# for key,value in D.items():
#   print(f"{key}: {value}")
# #Nestled Dictionary
# Student ={}
# Student['student1'] = {'name':'Sayantan','age':23,'grade':'A+'}
# Student['student2'] ={'name':'Diya','age':20,'grade':'A'}
# Student['student3'] ={'name':'Dabu','age':21,'grade':'A++'}
# print("Student_details")
# print(Student)
# #Accesing elements from nestled Dictionay
# print(Student['student1']['name'])
# print(Student['student3'])
# #Adding elements to nestled dictionary
# Student['student1']['phone_no'] ='8509991051'
# Student['student4'] ={'name':'priyanka','age':21,'grade':'c'}
# print("updated student details")
# print(Student)
# #Dlete Elements from nestled dictionary
# del Student ['student1']['phone_no']
# Student.pop('student4')
# print("new student details")
# print(Student)
# mydict = {
#   x:x**2 for x in [1,2,3,4,5]
  
# }
# print(mydict)
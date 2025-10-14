# numbers =  map (int, input("Enter numbers:").split(" "))  
# Even_square =[x **2 for x in numbers ]
# print(Even_square)
Even_square = [x**2 for x in range(5) if x**2%2 ==0]
print(Even_square)


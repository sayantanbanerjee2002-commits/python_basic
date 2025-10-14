# class fibonacciiterator:
#     def __init__(self,stop =10):
#         self.stop =stop
#         self.index =0
#         self.current =0
#         self.next =1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<self.stop:
#             self.index+=1
#             fibb_number =self.current
#             self.current, self.next =(self.next,self.current+self.next)
#             return fibb_number
#         else:
#             raise StopIteration
# fib =fibonacciiterator(10)
# for num in fib:
#     print(num) 
# mydict = {
#   x:x**2 for x in [1,2,3,4,5]
  
# }
# print(mydict)
#Even number iterator
class Even_number():
    def __iter__(self):
        self.n = 2
        return self
    
    def __next__(self):
        if self.n<=20:
            x =self.n
            self.n += 2
            return x
        else:
            raise StopIteration
        
even =Even_number()
it =iter(even)
for num in it:
    print(num)

        
        
        
    
    



        
        
        
        
        
    

 
    
    

    
    
     
        
        
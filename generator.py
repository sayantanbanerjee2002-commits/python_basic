# def even_number_generator(limit):
#     num =0
#     while num<=limit:
        
#         yield(num)
#         num +=2
# Evens =even_number_generator(18)
# for num in Evens:
#     print(num)
    
#fibbonacci series generator
def fibonacci_series_generator(stop):
    index = 0
    current = 0
    next =1
    while index<=stop:
        yield(current)
        
        current,next =(next, current+next)
        index +=1
        
fibbonacci =fibonacci_series_generator(7)  
for num in fibbonacci:
    print(num)
    
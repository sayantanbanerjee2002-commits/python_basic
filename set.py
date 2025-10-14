#difference between set
s1 =set({})
s2 =set({})
#add element in the set by iterable
for i in range(1,10):
 s1.add(i)
for i in range(6,15):
    s2.add(i)
new_set =s2-s1
print(new_set)
#union between set
s1 =set({})
s2 =set({})
for i in range(9,20):
    s1.add(i)
for i in range(10,25):
    s2.add(i)
new_set =s1.union(s2)
print(new_set)
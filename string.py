s1 = "Sayantan "
s2 =  "Banerjee"
print(s1+s2)
print(s1[5])
print(s2[-3])
print(s1[1:5]) #String slicing
print(s1[: :-1]) #reverse of the string
#string updatons
s = "Sayantan Banerjee"
#updating string
s = s[:8] + " kumar "+ s[9:]
print(s)
#delete string
del(s)
print(s)
s = 'Sayantan Banerjee'
S = s.replace("Sayantan", "Suman")
print(S)
print(len(s)) #length of the string
print(s.lower()) #lower case 


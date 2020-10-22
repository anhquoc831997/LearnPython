#Bai 44
s1 = input()
s2 = input()
t = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = t 
print(s1 + " " + s2)
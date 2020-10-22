#Bai 54
a = int(input())
b = int(input())
c = int(input())

if(a == b and b == c and c == a):
    print("Equilateral triangle")
elif(a == b and a == c) or (b == a and b == c) or (c == a and c == b):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

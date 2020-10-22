#Bai 32
a = int(input())
b = int(input())
sum = 0
while a <= b:
    if a % 2 != 0:
        sum += a
    a += 1
print(sum)
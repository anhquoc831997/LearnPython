#Bai 38
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
sum = 0
for t in lst:
    sum += t
print(sum)
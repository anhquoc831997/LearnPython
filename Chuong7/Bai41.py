#Bai 41
lst = []
n = int(input())

for i in range(n):
    lst.append(int(input()))

mang = []
for t in lst:
    if t % 5 == 0:
        mang.append(t)
if len(mang) == 0:
    mang = [0]

print(mang)
#Bai 40
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
so_le = []
for t in lst:
    if t %2 != 0:
        so_le.append(t)
print(so_le)

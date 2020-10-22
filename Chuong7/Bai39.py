#Bai 39
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(len(lst)):
    for j in range(i):
        if lst[i] < lst[j]:
            t = lst[i]
            lst[i] = lst[j]
            lst[j] = t
print(lst)
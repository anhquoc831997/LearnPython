#Bai 49.py
def get_unique_values(lst):
    mang = []
    for i in lst:
        if i not in mang:
            mang.append(i)
    return mang
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(get_unique_values(lst))
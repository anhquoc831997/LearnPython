#Bai 55
str = str(input())

def check(str):
    lst = str.split()
    mang = []
    for i in lst:
        if len(i) > 3:
            mang.append(i)
    return mang
print(check(str))
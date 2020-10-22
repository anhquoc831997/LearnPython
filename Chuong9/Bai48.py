#Bai 48
def show(s):
    in_hoa = 0
    in_thuong = 0
    for i in s:
        if i.isupper():
            in_hoa += 1
        if i.islower():
            in_thuong += 1
    print("Given string:", s)
    print("Number of uppercase letters:" , in_hoa)
    print("Number of lowercase letters:", in_thuong)
s = str(input())
show(s)
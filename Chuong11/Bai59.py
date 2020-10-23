#Bai 59
n = int(input())

def is_abundant(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    if sum(lst) > 2 * n:
        print("True")
    else: 
        print("False")
is_abundant(n)
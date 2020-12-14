#Bai 10
a = int(input())
b = int(input())

def gcd(a,b):
    if a == b:
        return a
    if a > b:
        a -= b
    else: b -= a
    return gcd(a,b)
print(gcd(a,b))
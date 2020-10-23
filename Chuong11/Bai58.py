#Bai 58
n = int(input())

def sumOfAll(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum
print(sumOfAll(n))
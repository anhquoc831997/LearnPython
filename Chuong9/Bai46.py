#Bai 46
def sum_of_list(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(sum_of_list(lst))
#Bai 51
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    s = []
    for i in res:
        if i % 2 == 0:
            s.append(i)
    return s
print(evenNum(res))

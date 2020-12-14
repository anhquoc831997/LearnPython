#Bai 57
s = str(input())

def format(s):
    if len(s) >= 3:
        if s[-3:] != "ing":
            print(s + "ing")
        else:
            print(s + "ly")
    else:   
        print (s)
format(s)
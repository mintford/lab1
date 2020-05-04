def myFact(num):
    res = 1
    for i in range(1,num+1):
        res = res * i
    return res
n = 2
print(myFact(n))
n = 4
print(myFact(n))
n = 6
print(myFact(n))


def isPalindrom(string):
    strn = str(string)
    a = len(strn)
    b = True
    for i in range(a):
        if strn[i] == strn[a-i-1]:
            b = True
        else:
            b = False
            break
    return b
str2 = "123321"
print(isPalindrom(str2))

str2 = "sasa"
print(isPalindrom(str2))

str2 = "oppo"
print(isPalindrom(str2))

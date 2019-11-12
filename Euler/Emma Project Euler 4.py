a = 100
b = 100
upperlimit = 999
fiveLimit = 100000

while a <= upperlimit and b <= upperlimit:
    c = a * b
    stringC = repr(c)
    while c < fiveLimit:
        stringC1 = stringC[0:2]
        stringC2 = stringC[2:5]
        if stringC1 == stringC2[::-1]:
            print("palindrome")
        else:
            a = a + 1
            print("a value" + str(a))
        b = b + 1
    else:
        stringC1 = stringC[0:3]
        stringC2 = stringC[3:6]
        if stringC1 == stringC2[::-1]:
            print("palindrome")
        else:
            a = a + 1
        b = b + 1


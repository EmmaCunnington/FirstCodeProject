upperlimit = 4000000

a = 1
b = 2
c = a + b
sum1 = 2

while (a < upperlimit) and (b < upperlimit) and (c < upperlimit):
    a = b + c
    if a >= upperlimit:
        break
    else:
        if a%2 == 0:
            sum1 = sum1 + a 
    print(a)
    print("sum1:" + str(sum1))
    
    b = a + c
    if b >= upperlimit:
        break
    else:
        if b%2 == 0:
            sum1 = sum1 + b
    print(b)
    print("sum1:" + str(sum1))
    
    c = a + b
    if c >= upperlimit:
        break
    else: 
        if c%2 == 0:
            sum1 = sum1 + c
    print(str(c) + "sum1:" + str(sum1))
    
    print("sum1:" + str(sum1))

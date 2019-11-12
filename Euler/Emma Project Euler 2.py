upperlimit = 4000000

a = 1
b = 2
c = a + b
sum1 = 2

while True:
    a = b + c
    if a >= upperlimit:
        break
    elif a%2 == 0:
        sum1 = sum1 + a 
    print(a)
    print("sum1:" + str(sum1))
    
    b = a + c
    if b >= upperlimit:
        break
    elif b%2 == 0:
        sum1 = sum([sum1,b])
    print(b)
    print("sum1:" + str(sum1))
    
    c = a + b
    if c >= upperlimit:
        break
    else: 
        if c%2 == 0:
            sum1 = sum1 + c
    print(str(c) + "sum1:" + str(sum1))
# Original script

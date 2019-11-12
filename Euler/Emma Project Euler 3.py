def isPrime(num):
    if num == 1 or num == 0:
        return False
    div = 2
    while div < num:
        if num%div  == 0:
            return False
        else: 
            div = div + 1
    return True

a = 600851475143
div = 2
while a > div:
    if a%div == 0 and isPrime(div):
        print("first number " + str(div))
    else:
        div = div + 1
        if isPrime(div) and a%div == 0:
            print("second number " + str(div))
        else:
            div = div + 1
            if isPrime(div) and a%div == 0:
                print("third number " + str(div))
    div = div + 1

#first try




    

            

        

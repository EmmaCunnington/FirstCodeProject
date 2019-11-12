def isPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    div = 3
    while div < num/2:
        if num%div  == 0:
            return False
        else: 
            div = div + 2
    return True

a = 600851475143
div = 3

while div < a:
    if a%div == 0:
        print("factor: " + str(div))
        a = a/div
        print("a" + str(a))
    else:
        div = div + 1




    

            

        

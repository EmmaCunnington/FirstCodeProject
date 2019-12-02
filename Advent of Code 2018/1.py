file = open("Advent of Code 2018/1 input.txt", "r")
change_array_string = file.read().split()
file.close()

test_array = [+7, +7, -2, -7, -4]

frequency = 0
frequency_array = {0}
isBroken = False
while not(isBroken):
    print("did this go twice")
    for change in change_array_string:
        change_int = int(change)
        frequency += change_int
        if (frequency in frequency_array):
            isBroken = True
            break
        else:
            frequency_array.add(frequency)


print(frequency in frequency_array)
print(frequency)




    

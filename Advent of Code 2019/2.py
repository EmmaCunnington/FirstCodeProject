file = open("Advent of Code 2019/2.txt", "r")
opcode_array_string = file.read().split(',')
file.close()

opcode_array_int = []
address_book = []

for opcode_string in opcode_array_string:
    opcode_int = int(opcode_string)
    opcode_array_int.append(opcode_int)
    address_book.append(opcode_int)

opcode_array_int[1] = 12
opcode_array_int[2] = 2

for i in range(len(opcode_array_int)//4):
    n = i * 4
    opcode = opcode_array_int[n]
    if opcode == 99:
        break
    elif opcode == 1:
        opcode_array_int[opcode_array_int[n+3]] = opcode_array_int[opcode_array_int[n+1]] + opcode_array_int[opcode_array_int[n+2]]
    elif opcode == 2:
        opcode_array_int[opcode_array_int[n+3]] = opcode_array_int[opcode_array_int[n+1]] * opcode_array_int[opcode_array_int[n+2]]
    else:
        print("Something has gone wrong")

print(opcode_array_int)

print(opcode_array_int[0])

##Part Two!

print('Part Two')
print(address_book)

old_address_book = address_book

for noun in range(100):
    for verb in range(100):
        address_book = old_address_book.copy()
        address_book[1] = noun
        address_book[2] = verb
        for i in range(len(address_book)//4):
            n = i * 4
            if address_book[n] == 99:
                break
            elif address_book[n] == 1:
                address_book[address_book[n+3]] = address_book[address_book[n+1]] + address_book[address_book[n+2]]
            elif address_book[n] == 2:
                address_book[address_book[n+3]] = address_book[address_book[n+1]] * address_book[address_book[n+2]]
            else:
                break
        if address_book[0] == 19690720:
            print('Yay!')
            print(noun)
            print(verb)
            print(100*noun+verb)

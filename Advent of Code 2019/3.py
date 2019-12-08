#two wires from central port outward
# find intersection of wire cross closest to central port using manhatten distance
# central port doesn't count, nor does a wire crossing itself
# what is manhatten distance from central port to the closes intersection?

# need to make an array (not like a list, a whole plane thing) and trace both wires across
# then find the intersection of different points (not central or one wire crossing itself)
# then add x and y coordinates of intersection points, the one with the lowest sum is lowest manhatten distance from (0, 0)

file = open("Advent of Code 2019/3.txt", "r")
split_wires = file.read().split()
wires = [wire.split(',') for wire in split_wires]
wire_1 = ['R8','U5','L5','D3']#wires[0]
wire_2 = ['U7','R6','D4','L4']#wires[1]
file.close()

wire_1_port_x = 0
wire_1_port_y = 0

wire_2_port_x = 0
wire_2_port_y = 0

coordinates_list_wire_1 = []
coordinates_list_wire_2 = []
intersection_list = []

for direction in wire_1:
    if direction[0] == 'L':
        wire_1_port_x -= int(direction[1:len(direction)])
    elif direction[0] == 'R':
        wire_1_port_x += int(direction[1:len(direction)])
    elif direction[0] == 'U':
        wire_1_port_y += int(direction[1:len(direction)])
    elif direction[0] == 'D':
        wire_1_port_y -= int(direction[1:len(direction)])
    else:
        print('Direction not recognised')
        break
    wire_1_coordinates = (wire_1_port_x, wire_1_port_y)
    coordinates_list_wire_1.append(wire_1_coordinates)

print('Wire 1')
print (coordinates_list_wire_1)

for direction in wire_2:
    if direction[0] == 'L':
        wire_2_port_x -= int(direction[1:len(direction)])
    elif direction[0] == 'R':
        wire_2_port_x += int(direction[1:len(direction)])
    elif direction[0] == 'U':
        wire_2_port_y += int(direction[1:len(direction)])
    elif direction[0] == 'D':
        wire_2_port_y -= int(direction[1:len(direction)])
    else:
        print('Direction not recognised')
        break
    wire_2_coordinates = (wire_2_port_x, wire_2_port_y)
    coordinates_list_wire_2.append(wire_2_coordinates)
    # doesn't find anything
    # if wire_2_coordinates in coordinates_list_wire_1 == True:
    #     intersection_list.append(wire_2_coordinates)
    # else:
    #     print('no intersections found')
    
print('Wire 2')
print (coordinates_list_wire_2)

print('finding intersections')

# doesn't find anything:
# for coordinates in coordinates_list_wire_1:
#     if coordinates in coordinates_list_wire_2:
#         intersection_list.append(coordinates)
#     else:
#         print('No intersection found')

print('Intersections')
print(intersection_list)
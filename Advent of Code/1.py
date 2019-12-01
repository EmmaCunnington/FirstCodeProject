# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, 
# divide by three, round down, and subtract 2.
# The Fuel Counter-Upper needs to know the total fuel requirement. 
# To find it, individually calculate the fuel needed for the mass of 
# each module (your puzzle input), then add together all the fuel values.
# What is the sum of the fuel requirements for all of the 
# modules on your spacecraft?

module_mass_string = """129192
58561
57267
95382
84995
127372
93598
97264
138550
79327
135661
139468
108860
149642
72123
128333
69002
98450
86267
70171
101333
79822
142539
142743
51371
111381
62073
72210
125168
135952
131060
121842
88234
146774
136571
126719
50644
75696
51195
77171
118052
83691
133779
149814
64847
110697
92695
59453
139517
129487
79271
97896
146987
149822
71866
90797
104732
54997
50139
134115
133017
144979
89428
124750
91833
57252
67195
121624
102706
138245
127700
124098
110382
121557
103613
133576
122801
112306
120203
134696
76129
84576
80854
147237
71025
127513
143631
125090
115698
57979
84880
120177
147389
88380
114688
56355
126265
58220
63523
130179"""

def fuel_required(mass):
    fuel = (mass//3) - 2
    if fuel < 0:
        return 0
    return fuel + fuel_required(fuel)

modules_mass = str.split(module_mass_string)

fuel_module_array = []

for module in modules_mass:
    integer_mass = int(module)
    module_fuel = fuel_required(integer_mass)
    fuel_module_array.append(module_fuel)

fuel_required = sum(fuel_module_array)
print(fuel_required)


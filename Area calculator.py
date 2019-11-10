'''This program will compute the area of triangles and circles. It will:
 - prompt the user to select a shape,
 - calculate the area of the shape,
 - print the area of the shape.'''

print ('Area calculator is starting!')

option = (input('Enter C for Circle or T for Triangle: ')).upper()

if option == 'C': 
  radius = float(input('Please enter the radius of the circle: '))
  area = 3.14159 * radius ** 2
  print ('The area of the circle is %s' % (area))
  
elif option == 'T':
  base = float(input('Please enter the base of the triangle: '))
  height = float(input('Please enter the height of the triangle: '))
  area = base * height * 0.5
  print ('The area of the triangle is %s' % (area))
  
else:
  print ('Invalid response. Please enter either C or T')
  
print ('Thanks for using Area Calculator')

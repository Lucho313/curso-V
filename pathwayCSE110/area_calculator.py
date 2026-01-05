# square area

square_size = float(input("What is the length of a side of the square in cm? "))

square_area = square_size**2
square_size_in_meters = square_size / 100
square_area_in_meters = square_size_in_meters**2


print(f"The area of the square in cm^2 is:{square_area}")
print(f"The area of the square in m^2 is:{square_area_in_meters}")

# rectangle area

rectangle_length = float(input("What is the length of the rectangle in cm? "))
rectangle_width = float(input("what is the width of the rectangle in cm? "))

rectangle_area = rectangle_length * rectangle_width
rectangle_area_in_meters = rectangle_length / 10000


print(f"The area of the rectangle in cm^2 is: {rectangle_area}")
print(f"The area of the rectangle in m^2 is: {rectangle_area_in_meters}")

# circle area

circle_radius = float(input("What is the radius of the circle in cm? "))
radius_squared = circle_radius**2
PI_NUMBER = 3.14
Circule_area = radius_squared * PI_NUMBER
circle_area_in_meters = Circule_area / 10000

print(f"The area of the circle in cm^2 is: {Circule_area}")
print(f"The area of the circle in m^2 is: {circle_area_in_meters}")




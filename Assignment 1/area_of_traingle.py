def area_of_triangle(base, height):
    return 0.5 * base * height

base = float(input("Enter base of a triangle: "))
height = float(input("Enter height of a triangle: "))

area = area_of_triangle(base, height)
print(area)
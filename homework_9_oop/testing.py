import classes

# class Point:

p1 = classes.Point(5, 30)
p2 = classes.Point(-10, 10)
p3 = p1 + p2
p4 = p2 - p1

print(f'p3 coordinates {p3.get_coordinates()}')
print(f'p4 coordinates {p4.get_coordinates()}')


# class Triangle:

t1 = classes.Triangle(-11, 25, -86, 39, 47, 2)
print(f'Triangle area: {t1.get_area()}')
print(f'Triangle perimeter: {t1.get_perimeter()}')
t1.set_apex('b', 12, 11)
# print(t1.a.get_coordinates())


class Shape:
    """
    Base class for Circle and Point
    Shape.__init__ sets Shape's center
    """

    @staticmethod
    def validator(*args):
        """
        Validate Shapes parameters
        :param args: coordinates or radius
        :return: bool
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise AttributeError(f'wrong coordinate {arg}')
        return True

    def __init__(self, x, y):
        if Shape.validator(x, y):
            self.x = x
            self.y = y


class Point(Shape):
    """
    simple point with X and Y
    """
    pass


class Circle(Shape):
    """
    Circle has center (x, y)
    and radius (r)
    """
    def __init__(self, x, y, r):
        super().__init__(x, y)
        if Circle.validator(r):
            self.radius = r

    def contains(self, point):
        """
        Checks, if Circle contains point
        :param point: class Point object
        :return: bool
        """
        if isinstance(point, Point) and \
                (point.x - self.x) ** 2 + \
                (point.y - self.y) ** 2 <= \
                self.radius ** 2:
            return True
        else:
            return False

    def __contains__(self, item):
        return self.contains(item)


# TESTS:
p = Point(8.1, -6)
c = Circle(16, 11, 25)
c2 = Circle(11, -25, 3)

print(c.contains(p))
print(p in c)
print(c2 in c)

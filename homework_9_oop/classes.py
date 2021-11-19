class Point:
    def __init__(self, x, y):
        if Point.int_validator(x, y):
            self._x = x
            self._y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self._x + other._x, self._y + other._y)
        else:
            raise AttributeError(f'only point + point supported')

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self._x - other._x, self._y - other._y)
        else:
            raise AttributeError(f'only point - point supported')

    @staticmethod
    def int_validator(*args):
        for arg in args:
            if type(arg) != int:
                raise AttributeError(f'Wrong coordinate {arg}')
        return True

    def _change_position(self, x, y):
        self._x = x
        self._y = y

    def get_coordinates(self):
        return self._x, self._y

    def set_coordinates(self, x, y):
        if Point.int_validator(x, y):
            self._change_position(x, y)


class Triangle:

    def __init__(self, ax, ay, bx, by, cx, cy):
        if Point.int_validator(ax, ay, bx, by, cx, cy):
            self.a = Point(ax, ay)
            self.b = Point(bx, by)
            self.c = Point(cx, cy)

    def _get_points(self):
        """
        Some methods need apex coordinates
        :return: x and y for each apex
        """
        (ax, ay), (bx, by), (cx, cy) = (point.get_coordinates() for point in self.__dict__.values())
        return ax, ay, bx, by, cx, cy

    def get_area(self):
        ax, ay, bx, by, cx, cy = self._get_points()
        return abs(((ax - cx) * (by - cy) - (bx - cx) * (ay - cy)) * 0.5)

    def get_perimeter(self):
        ax, ay, bx, by, cx, cy = self._get_points()
        a = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
        b = ((cx - bx) ** 2 + (cy - by) ** 2) ** 0.5
        c = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5
        return round(a + b + c, 2)

    def set_apex(self, apex, x, y):
        """
        Sets new coordinates for apexes
        :param apex: a/b/c
        :param x: new X coordinate (int)
        :param y: new Y coordinate (int)
        """
        if apex in self.__dict__:
            self.__dict__[apex].set_coordinates(x, y)
        else:
            raise AttributeError(f'Object has no apex {apex}')

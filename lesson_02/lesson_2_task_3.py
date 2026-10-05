import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        return math.ceil(area)
    return area


print(square(5))

import math


def calc_distance(a, b):
    distance = math.sqrt(a**2 + b**2)
    return distance


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


data_first_point = input().split()
data_second_point = input().split()

first_x = int(data_first_point[0])
first_y = int(data_first_point[1])
second_x = int(data_second_point[0])
second_y = int(data_second_point[1])

first_point = Point(first_x, first_y)
second_point = Point(second_x, second_y)

side_a = abs(first_point.x - second_point.x)
side_b = abs(first_point.y - second_point.y)

side_c = calc_distance(side_a, side_b)

print(f"{side_c:.3f}")
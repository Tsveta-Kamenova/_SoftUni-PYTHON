import math


def calculate_perimeter(w, h):
    perimeter = 2*w + 2*h
    return perimeter


def calculate_area(w, h):
    area = w*h
    return area


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point_2):
        a = abs(self.x - point_2.x)
        b = abs(self.y - point_2.y)
        distance = math.sqrt(a**2 + b**2)
        return distance


list_points_input = input().replace(" | ", ":").split(":")

while len(list_points_input) != 1:
    p1_x = int(list_points_input[0])
    p1_y = int(list_points_input[1])
    p2_x = int(list_points_input[2])
    p2_y = int(list_points_input[3])
    p3_x = int(list_points_input[4])
    p3_y = int(list_points_input[5])
    p4_x = int(list_points_input[6])
    p4_y = int(list_points_input[7])

    upper_left = Point(p1_x, p1_y)
    upper_right = Point(p2_x, p2_y)
    bottom_left = Point(p3_x, p3_y)
    bottom_right = Point(p4_x, p4_y)

    width = upper_left.calculate_distance(upper_right)
    height = upper_left.calculate_distance(bottom_left)
    perimeter = 2*(width+height)
    area = width*height

    print(f"Box: {width:.0f}, {height:.0f}")
    print(f"Perimeter: {perimeter:.0f}")
    print(f"Area: {area:.0f}")

    list_points_input = input().replace(" | ", ":").split(":")


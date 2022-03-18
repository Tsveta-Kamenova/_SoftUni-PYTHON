import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Distance:
    def __init__(self, p1, p2, length):
        self.p1 = p1
        self.p2 = p2
        self.length = length


def calc_distance(x1, x2, y1, y2):
    a1 = abs(x1 - x2)
    b1 = abs(y1 - y2)
    distance = math.sqrt(a1**2 + b1**2)
    return distance


list_points = []
list_distances = []
min_distance = float("inf")

n = int(input())

for i in range(n):
    data_current_point = input().split()

    current_x = int(data_current_point[0])
    current_y = int(data_current_point[1])
    current_point = Point(current_x, current_y)

    list_points.append(current_point)

for i in range(0, len(list_points)-1):
    for j in range(i+1, len(list_points)):
        current_distance = Distance(list_points[i], list_points[j], calc_distance(list_points[i].x, list_points[j].x,
                                                                                  list_points[i].y, list_points[j].y))
        list_distances.append(current_distance)

for i in range(0, len(list_distances)):
    if list_distances[i].length < min_distance:
        min_distance = list_distances[i].length
        p1_min = list_distances[i].p1
        p2_min = list_distances[i].p2
    else:
        pass

print(f"{min_distance:.3f}")
print(f"({p1_min.x}, {p1_min.y})")
print(f"({p2_min.x}, {p2_min.y})")
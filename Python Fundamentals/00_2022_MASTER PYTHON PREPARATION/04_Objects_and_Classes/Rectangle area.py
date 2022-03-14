class Rectangle:
    def __init__(self, width, height):
        self._width = self.set_width(width)
        self._height = height

    def calc_area(self):
        area = self._width*self._height
        return area

    def set_width(self, width):
        if not (type(width) is int):
            return int(width)
        else:
            return width


data_input = list(map(int, input().split()))
w = data_input[0]
h = data_input[1]

my_rectangle = Rectangle(width=w, height=h)
print(my_rectangle.calc_area())
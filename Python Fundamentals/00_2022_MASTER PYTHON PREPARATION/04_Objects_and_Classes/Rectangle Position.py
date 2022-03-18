class Rectangle:
    def __init__(self, left, top, width, height, right, bottom):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = right
        self.bottom = bottom

    def is_inside(self, r2):
        if (self.left >= r2.left) and (self.right <= r2.right) and (self.top <= r2.top) and (self.bottom <= r2.bottom):
            print("Inside")
        else:
            print("Not inside")


list_rectangles = []

for i in range(2):
    data_input = list(map(float, input().split()))

    current_left = data_input[0]
    current_top = data_input[1]
    current_width = data_input[2]
    current_height = data_input[3]

    current_right = current_left + current_width
    current_bottom = current_top + current_height

    current_rectangle = Rectangle(current_left, current_top, current_width, current_height, current_right,
                                  current_bottom)

    list_rectangles.append(current_rectangle)


Rectangle.is_inside(list_rectangles[0], list_rectangles[1])
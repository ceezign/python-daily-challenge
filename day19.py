# python class that models a rectangle


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("height and width must be positive")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_squared(self):
        return self.width == self.height

    def __str__(self):
        return f"rectangle {self.width} x {self.height}"

rect1 = Rectangle(4, 5)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
print("Is Squared:", rect1.is_squared())

rect2 = Rectangle(6, 6)
print(rect2, "is Squared?", rect2.is_squared())

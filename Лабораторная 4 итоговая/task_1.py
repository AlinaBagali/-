class Shape:
    def __init__(self, color: str):
        self.color = color

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
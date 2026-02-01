class Shape:
    def __init__(self):
        self.__color = None

    @property
    def color(self):
        """Get the color of the shape."""
        return self.__color

    @color.setter
    def color(self, value):
        """Set the color only if it's a string, otherwise raise TypeError."""
        if not isinstance(value, str):
            raise TypeError("Color must be a string")
        self.__color = value


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height


if __name__ == "__main__":
    shapes = [Rectangle(2, 3), Circle(5), Triangle(3, 4)]

    for s in shapes:
        try:
            s.color = "blue"  # poprawne przypisanie
            print(f"{s.__class__.__name__} color set to {s.color}")

            s.color = 123  # niepoprawne przypisanie
        except TypeError as e:
            print(f"Error: {e}")
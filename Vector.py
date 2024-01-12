import math

class Vector:
    x: int
    y: int

    def from_axis(x: int, y: int):
        result: Vector = Vector()
        result.x = x
        result.y = y
        return result

    def from_vector(other):
        result: Vector = Vector.from_axis(other.x, other.y)
        return result
    
    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # Addition, subtraction, multiplication, division

    def __add__(self, other):
        x: int = self.x + other.x
        y: int = self.y + other.y
        result: Vector = Vector.from_axis(x, y)
        return result
    
    def __sub__(self, other):
        x: int = self.x - other.x
        y: int = self.y - other.y
        result: Vector = Vector.from_axis(x, y)
        return result
    
    def __mul__(self, other):
        x: int = self.x * other.x
        y: int = self.y * other.y
        result: Vector = Vector.from_axis(x, y)
        return result
    
    def __truediv__(self, other):
        x: int = self.x / other.x
        y: int = self.y / other.y
        result: Vector = Vector.from_axis(x, y)
        return result
    
    def __floordiv__(self, other):
        x: int = self.x // other.x
        y: int = self.y // other.y
        result: Vector = Vector.from_axis(x, y)
        return result
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)
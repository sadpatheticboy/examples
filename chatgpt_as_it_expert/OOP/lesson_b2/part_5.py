# My solution:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __matmul__(self, other):  # ChatGPT added this
        return self.x * other.x + self.y * other.y


# Tests
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)  # Vector(1, 2)
print(v2)  # Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(-2, -2)
print(v1 * v2)  # 11

# ChatGPT added this
v1 = Vector(1, 2)
v2 = Vector(3, 4)
dot_product = v1 @ v2
print(dot_product)  # Output: 11

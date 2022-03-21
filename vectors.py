import math


class Vec2d:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '({},{})'.format(self.a, self.b)

    def len(self):
        return int(math.sqrt(self.a ** 2 + self.b ** 2))


    def __add__(self, other):
        return Vec2d(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vec2d(self.a - other.a, self.b - other.b)

    def __rmul__(self, other):
        return Vec2d(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Vec2d(self.a / other.a, self.b / other.b)

    def scalar(self, scalar_value):
        return self.a * scalar_value, self.b * scalar_value

    def dot(self, other):
        return self.a * other.a + self.b * other.b




vector_1 = Vec2d(12, 45)

vector_2 = Vec2d(16, 31)

vector_3 = Vec2d(1, 13)

vector_4 = Vec2d(0, -1)

result_vector = vector_4.scalar(5)
vector_summ = vector_3.dot(vector_4)
vector_normalize = vector_2.len()
print(vector_normalize)
print(result_vector)
print(vector_summ)


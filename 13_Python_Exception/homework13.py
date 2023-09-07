from Error import NegativeSide, ErroneousData

class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise NegativeSide(self.a, b, c)
        if self.a > self.b + self.c or self.b > self.a + self.c \
                or self.c > self.a + self.b:
            raise ErroneousData(self.a, b, c)

    def check(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return f"Треугольник разносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return f"Треугольник равнобедренный"

test = Triangle(6, 2, 3)
print(test.check())
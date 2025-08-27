import math
import random

class Vector2:
    # //ai
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x,
                       self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x,
                       self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar,
                       self.y * scalar)

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector2(self.x / scalar,
                           self.y / scalar)
        raise ValueError("Cannot be divided by zero!")

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return self / mag
        return Vector2(0, 0)


class Random:
    def __init__(self):
        pass

    def seed(self, value=None):
        random.seed(value)
            
        
    def randsp(self, surface, a=0):
        return (
            random.randint(a, surface.w - 1),
            random.randint(a, surface.h - 1)
        )

    def randpos(self, b=-900, a=900):
        x = random.randint(b, a) * random.choice([-1, 1])
        y = random.randint(b, a) * random.choice([-1, 1])
        return (x, y)  

    def randint(self, a, b):
        return random.randint(a, b)

    def randfloat(self, a=0.0, b=1.0):
        return random.uniform(a, b)

    def randcolor(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def randchoice(self, seq):
        return random.choice(seq)

    def randbool(self):
        return random.choice([True, False])

    def randsign(self):
        return random.choice([-1, 1])

    def randangle(self, deg=False):
        return random.uniform(0, 360) if deg else random.uniform(0, 2 * 3.14159)
rand = Random()

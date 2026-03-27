class PointStandard:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointOptimized:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = PointStandard(1, 2)
p2 = PointOptimized(1, 2)


p1.z = 100
p2.z = 100 # Rzuci AttributeError!




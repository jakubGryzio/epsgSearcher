import math


class Point():
    def __init__(self, location):
        self.x = location[1]
        self.y = location[0]

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    def calc_distance(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2) / 1000

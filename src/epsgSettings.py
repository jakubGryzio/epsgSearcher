from helpers.config import *
from helpers.texts import *


class epsgSettings():
    thresh_distance_2180 = 700
    thresh_distance_2175 = 500

    def __init__(self, point):
        self.point = point

    def get_EPSG(self):
        if self.check_how_many_coords_numbers(6):
            if self.is_EPSG2180():
                return epsg_2180
            if self.is_EPSG2175():
                return epsg_2175
            return epsg_error
        if self.check_how_many_coords_numbers(7):
            if self.is_EPSG2176():
                return epsg_2176
            if self.is_EPSG2177():
                return epsg_2177
            if self.is_EPSG2178():
                return epsg_2178
            if self.is_EPSG2179():
                return epsg_2179
            return self.is_1965()
        return epsg_error

    def check_how_many_coords_numbers(self, number):
        # checking if coords have a some digit of numbers
        return len(str(int(self.point.x))) == number and len(str(int(self.point.y))) == number

    def is_EPSG2180(self):
        # checking possibility of epsg 2175
        return max([self.point.calc_distance(epsg_2180Point)
                    for epsg_2180Point in EPSG_2180Points]) < self.thresh_distance_2180

    def is_EPSG2175(self):
        return max([self.point.calc_distance(epsg_2175Point)
                    for epsg_2175Point in EPSG_2175Points]) < self.thresh_distance_2175

    def is_EPSG2176(self):
        # checking if first Y number is 5
        return str(self.point.y)[0] == yFirstDigit2176

    def is_EPSG2177(self):
        # checking if first Y number is 6
        return str(self.point.y)[0] == yFirstDigit2177

    def is_EPSG2178(self):
        # checking if first Y number is 7
        return str(self.point.y)[0] == yFirstDigit2178

    def is_EPSG2179(self):
        # checking if first Y number is 8
        return str(self.point.y)[0] == yFirstDigit2179

    def is_1965(self):
        distance = {epsg: self.point.calc_distance(ref_point)
                    for epsg, ref_point in refs_65.items()}
        return min(distance.items(), key=lambda elem: elem[1])[0]

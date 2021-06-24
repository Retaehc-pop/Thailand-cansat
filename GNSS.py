import math


class Coord:
    def __init__(self, lat_g=0, lng_g=0, lat_c=0, lng_c=0, alt_g=0, alt_c=0, gx=0, gy=0, gz=0):
        self.lat_g = math.radians(float(lat_g))
        self.lat_c = math.radians(float(lat_c))
        self.lng_g = math.radians(float(lng_g))
        self.lng_c = math.radians(float(lng_c))
        self.dlon = self.lng_c - self.lng_g
        self.dlat = self.lat_c - self.lat_g

        self.alt_g = float(alt_g)
        self.alt_c = float(alt_c)
        self.alt = self.alt_c - self.alt_g

        self.gx = float(gx)
        self.gy = float(gy)
        self.gz = float(gz)

    def arc(self):
        a = (math.sin(self.dlat / 2) ** 2)
        a += (math.cos(self.lat_g) * math.cos(self.lat_c) * ((math.sin(self.dlon / 2)) ** 2))
        x = math.sqrt(a)
        y = math.sqrt(1 - a)
        c = 2 * math.atan2(x, y)
        return c

    def ground_distance(self):
        R0 = 6371000
        d = R0 * self.arc()
        return d

    def line_of_sight(self):
        R0 = 6371000
        R = R0 + self.alt_g
        baselength = 2 * R * math.cos((math.pi - self.arc()) / 2)
        heightlength = self.alt

        los = baselength ** 2 + heightlength ** 2 - 2 * baselength * heightlength * math.cos((math.pi + self.arc()) / 2)
        los = math.fabs(los)
        los = math.sqrt(los)

        return los

    def azimuth(self):
        a = math.sin(self.dlon) * math.cos(self.lat_c)
        b = math.cos(self.lat_g) * math.sin(self.lat_c) - math.sin(self.lat_g) * math.cos(self.lat_c) * math.cos(self.dlon)
        theta = math.atan2(a, b)
        theta = math.degrees(theta)
        return theta

    def heading(self):
        ht = self.azimuth() - self.gz
        ht = ht % 360
        return ht

    def elevation(self):
        elev = math.atan2(self.alt, self.ground_distance())
        elev = math.degrees(elev)
        elev = elev - self.gx
        elev = elev % 360
        return elev

    def roll(self):
        ty = self.gy
        ty = ty % 360
        return ty

    def half(self):
        pass

    def pythagorus(self):
        pyx = math.atan2((self.lng_c - self.lng_g), (self.lat_c-self.lat_g))
        return pyx * 180/math.pi


if __name__ == '__main__':
    test = Coord(15.0, 100.11, 15.5, 100.41, 20.1, 25600.2, 1.0, -3.0, 8.0)
    print(test.ground_distance())
    print(test.line_of_sight())
    print(test.azimuth())
    print(test.pythagorus())

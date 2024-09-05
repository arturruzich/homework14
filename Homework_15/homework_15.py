class Rhombus:
    def __init__(self, side_a, angle_a):
        self.setattr('side_a', side_a)
        self.setattr('angle_a', angle_a)

    def setattr(self, name, value):
        if name == 'side_a':
            if value > 0:
                self.__dict__[name] = value
            else:
                raise ValueError

        elif name == 'angle_a':
            if 0 < value < 180:
                self.__dict__[name] = value
                self.__dict__['angle_b'] = 180 - value
            else:
                raise ValueError

    def __repr__(self):
        return f"Rhombus wits side {self.side_a} and angles {self.angle_a} and {self.angle_b}"

romb = Rhombus(10, 80)
print(romb)

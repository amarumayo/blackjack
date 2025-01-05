

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def calc_area(self):
        self.area = self.diameter * 3.1415
        return(self.area)


circle = Circle(10)

circle.calc_area()

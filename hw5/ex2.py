class Circle:
    radius = None
    def __init__(self, radius):
        self.radius = radius
        self.get_radius()

    def get_radius (self):
        print('Радиус круга =', self.radius)

    def set_radius (self):
        print('Установите новый радиус:')
        self.radius = input()

circle1 = Circle(17)
circle1.set_radius()
circle1.get_radius()
class Shape():
    """
    Base shape class for physicalPython
    
    xPos: Initial shape x position
    yPos: Initial shape y position
    zPos: Initial shape z position
    """
    def __init__(self, xPos = 0, yPos = 0, zPos = 0):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos

    def draw(self):
        """
        Draws this shape object on a given canvas
        """
        pass

    def isTouching(self, shape2):
        pass

class Sphere(Shape):
    """
    Sphere shape class for physicalPython

    xPos: Initial shape x position
    yPos: Initial shape y position
    zPos: Initial shape z position
    radius: The radius of the given sphere
    """

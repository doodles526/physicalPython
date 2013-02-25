class Vector(object):
    """
    Custom Vector class

    Could not find a Vector package with nescessary functionality
    No clue why this doesn't exist yet...
    """

    def __init__(self, *args, **kargs):
        """
        args are the individual coordinate values ie x, y, z
        Can have a vector of any dimension
        """
        #Might should add a TypeError if there are non number args
        if isinstance(args[0], (tuple, list)):
            self.position = list(args[0])
        else: 
            self.position = list(args)

    def printVector(self):
        """
        Print the vector
        """
        print self.position




    #Accessors/Mutators#
    def getPoint(self, index):
        """
        Gets the value in the position tuple of given index
        Assumes the user will use 1 for the first coor
        """
        return self.position[index-1]
    
    def setPoint(self, index, value):
        """
        Sets an index in position to the given value
        Assumes the user will use 1 for the first coor
        """
        self.position[index - 1] = value






    #OVERRIDES#

    def __eq__(self, other):
        """
        override equals operator
        """
        return self.position == other.position

    def __abs__(self):
        """
        override absolute value function
        """
        return Vector(tuple([abs(coor) for coor in self.position]))
    
    def __add__(self, other):
        """
        implements the addition operator
        """
        if len(self.position) != len(other.position):
            raise ValueError ("The vectors you are trying to add are of different Dimensions")
        
        else:
            return Vector([self.position[i] + other.position[i] for i in range(len(self.position))])

    def __sub__(self, other):
       if len(self.position) != len(other.position):
           raise ValueError ("The vectors you are trying to add are of different Dimensions")
       else:
           return Vector([self.position[i] - other.position[i] for i in range(len(self.position))])

    def __mul__(self, other):
        """
        multiple a vector with a scalar
        """
        if isinstance(other, (int, long, float)):
            raise ValueError ("Must multiply by int, long, or float.  Use dot or cross methods for vector-vector multiplication") 
        
        else:
            return Vector([coor * other for coor in self.position])

    def __div__(self, other):
        """
        divide vector by a scalar
        """
        if not isinstance(other, (int, long, float)):
            raise ValueError ("You must divide by an int, long, or float") 
        
        else:
            return Vector([float(coor) / other for coor in self.position])

    def __mod__(self, other):
        pass 


    def __len__(self):
        """
        overrides len function to return dimension of the vector
        """
        return len(self.position)

class Vector2D(Vector):
     
    def __init__(self, x, y):
        """
        Use Super's constructor and add x, y variables for easy access
        """
        Vector.__init__(self, x, y)

    #Accessors/Mutators#

    def __getattribute__(self, name):
        if name == 'x':
            return object.__getattribute__(self, 'position')[0]
        elif name == 'y':
            return object.__getattribute__(self, 'position')[1]
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'x':
            old = self.position
            old[0] = value
            object.__setattr__(self, 'position', old)
        elif name == 'y':
            old = self.position
            old[1] = value
            object.__setattr__(self, 'position', old)
        else:
            object.__setattr__(self, name, value)

class Vector3D(Vector):
    def __init__(self, x, y, z):
        Vector.__init__(self, x, y, z)
        self.x = x
        self.y = y
        self.z = z

    #Accessors and Mutators#

    def getX(self):
        """
        returns value of x
        """
        return self.x

    def getY(self):
        """
        return value of y
        """
        return self.y
    
    def getZ(self):
        """
        return value of z
        """
        return self.z

    def setX(self):
        """
        sets the value of z
        """
        self.set

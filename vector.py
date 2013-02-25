class Vector():
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
            self.position = tuple(args[0])
        else: 
            self.position = args

    def printVector(self):
        """
        Print the vector
        """
        print self.position




    #Accessors/Mutators#
    def getPoint(self, index):
        """
        Gets the value in the position tuple of given index
        """
        return self.position[index-1]
    






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

class DVector(Vector):
     
    def __init__(self, x, y):
        Vector.__init__(self, x, y)
        self.x = x
        self.y = y

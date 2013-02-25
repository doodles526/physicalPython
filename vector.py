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
            self.position = args[0]
        else: 
            self.position = args

    def getPoint(self, num):
        """
        get a certain coordinate based on number
        """
        return self.position[num - 1]

    def printVector(self):
        """
        Print the vector
        """
        print self.position

    def __eq__(self, other):
        """
        override equals operator
        """
        return self.position == other.position

    def __abs__(self):
        """
        override absolute value function
        """
        return tuple([abs(coor) for coor in self.position])
    
    def __add__(self, other):
        """
        implements the addition operator
        """
        if len(self.position) != len(other.position):
            raise ValueError ("The vectors you are trying to add are of different Dimensions")
        
        else:
            return tuple([self.position[i] + other.position[i] for i in range(len(self.position))])

    def __sub__(self, other):
       pass 

    def __len__(self):
        """
        overrides len function to return dimension of the vector
        """
        return len(self.position)

    










from numpy inport array
import Field

NUMBER_OF_VARIABLES = 10

class Monomial:
    coeff_and_index = array([0,0])
    def __init__(self,[i,index]):
        self.coeff_and_index = array([i,index])

def IndexToPower(index):
    return ???

class Polynomial:
    coeff = array([0 for i in xrange(NUMBER_OF_VARIABLES)])

    def __init__(self,numbers):
        self.coeff = numbers[:]

    def LT(self):
        index = 0
        for i in coeff:
            if i != 0:
                return [i,index]
            index += 1

def Add(poly1,poly2):
    return Field.Add(poly1.coeff, poly2.coeff)

def Mult(poly1,poly2):
    print "not yet"

def LCM(poly1,poly2):

def Devide(poly1,poly2):

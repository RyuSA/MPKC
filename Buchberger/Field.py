# coding utf-8;

FIELD_NUMBER = 31

MULT_TABLE = [[0 for i in xrange(FIELD_NUMBER)] for j in xrange(FIELD_NUMBER)]
INVERSE_TABLE = [0 for i in xrange(FIELD_NUMBER)]

def Create_Multiplication_Table():
    var = 0
    for i in xrange(FIELD_NUMBER-1):
        for j in xrange(i,FIELD_NUMBER):
            var = (i*j)%FIELD_NUMBER
            MULT_TABLE[i][j] = var
            MULT_TABLE[j][i] = var
            if var == 1:
                INVERSE_TABLE[i] = j
                INVERSE_TABLE[j] = i
    del var

def Add(a,b):
    return (a+b)%FIELD_NUMBER

def Mult(a,b):
    return MULT_TABLE[a][b]

def Reverse(a):
    if a == 0:
        return False
    else:
        return INVEERSE[a]

# print MULT_TABLE
# Create_Multiplication_Table()
# print MULT_TABLE

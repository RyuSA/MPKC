#coding UTF-8;
Field_NUM = 31



def Add(a,b):
    return (a+b)%Field_NUM

def Mult(a,b):
    return (a*b)%Field_NUM

def Create_Multiplication_Table():
      int var = 0;
      for(i in xrange(Field_NUM)):
        for(j = 0 in xrange(Field_NUM)):
          var = (i*j) % Field_NUM
          Mult_Table[i][j] = var
          Mult_Table[j][i] = var
          if(var == 1){
            Mult_Inverse[i] = j
            Mult_Inverse[j] = i

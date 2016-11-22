#include <iostream>
#include <vector>
using namespace std;

/*
field : GF31
Variable : 10
Equation : 20
 */
// typedef unsigned char BYTE;
const int Field_NUM = 31;
const int Variables = 10;
const int Number_of_terms = 45;
const int Equations = 20;

int Mult_Table[Field_NUM][Field_NUM];
int Mult_Inverse[Field_NUM];

int Add(int a, int b){
  return (a+b)%Field_NUM;
}

int Mult(int a, int b){
  return Mult_Table[a][b];
}

int Inverse(int a){
  return Mult_Inverse[a];
}

class Polynomial{
  public:

    std::vector<int> poly;

  Polynomial(int (&coff)[Number_of_terms]){
    poly = std::vector<int>(coff , std::end(coff));
  }

  void operator + (Polynomial Poly2){
    for(int i = 0; i < Field_NUM ; i++){
      this->poly[i] = Add( (this->poly)[i] , (Poly2.poly)[i] );
    }
  }
};

void Create_Multiplication_Table(){
  int var = 0;
  for(int i = 0 ; i < Field_NUM; i++){
    for(int j = 0 ; j < Field_NUM; j++){
      var = (int)((i*j) % Field_NUM);
      Mult_Table[i][j] = var;
      Mult_Table[j][i] = var;
      if(var == 1){
        Mult_Inverse[i] = j;
        Mult_Inverse[j] = i;
      }
    }
  }
}

int main(int argc, char const *argv[]) {
  Create_Multiplication_Table();
  int cofficient[] = {0,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4};
  Polynomial a = Polynomial(cofficient);
  for(int i = 0; i < Number_of_terms ; i++){
      cout << (a.poly)[i] << endl;
  }

  char en;
  cin >> en;
  return 0;
}

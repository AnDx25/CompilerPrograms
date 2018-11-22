
/*
A -> I = E | E

E -> P O P | P

O -> + | - | * | / | **

P -> I | L | UI | UL | (E)

U -> + | - | !

I -> C | CI

C -> a | b | ... | y | z

L -> D | DL

D -> 0 | 1 | ... | 8 | 9
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int value;
string app;

bool A(void);
bool I(void);
bool E(void);
bool P(void);
bool O(void);
bool L(void);
bool U(void);
bool C(void);
bool D(void);






int main(){
    
    cout << "A -> I = E |E" << app << endl;
    cout << "E -> P O P | P" << app << endl;
    cout << "O -> + | - | * | / | **" << app << endl;
    cout << "P -> I | L | UI | UL | (E)" << app << endl;
    cout << "U -> + | - | !" << app << endl;
    cout << "I -> C | CI" << app << endl;
    cout << "C -> a | b | ... | y | z " << app << endl;
    cout << "L -> D | DL" << app << endl;
    cout << "D -> 0 | 1 | ... | 8 | 9 " << app << endl;
    cout << " " << app << endl;
    
        ifstream document ("input.txt");
    
        if (document.is_open())
        {
            while (!document.eof())
            {
                value = 0;
                getline(document, app);
                cout << "String that was read from text file: " << app << endl;
                
                
                if (A())
                {
            cout << "The string's in the language\n" << endl;
                }
                else
                {
            cout << "The string is not in the language\n" << endl;
                }
            }
            document.close();
            }
        return 0;
       }

//***************************

      bool A()
      {
       if (I())
       {
        if (value < app.length() && app[value] == '=')
        {
            ++value;
            if (E()){
                    return true;
                      }
                    }
                  }
                 return false;
                  }

//***************************

        bool E()
        {
         if (P())
         {
             ++value;
             if(O())
             {
                 return true;
             }
             
             else if(P())
             {
                 return true;
             }}
            return false;
             {
                 
             }
        }

            
            //***************************
             

            bool O()
            {
                if(app[value] == '+' || app[value] == '-' || app[value] == '*' || app[value] == '/' || app[value] == '**'){
                
                    ++value;
                    return true;
                }
                 return false;
                }



             bool P()
             {
                 if (I())
                 {
                     return true;
                 }
                 else if (L())
                 {
                     return true;
                 }
                 else if(U())
                 {
                     ++value;
                     if(I())
                     {
                         return true;
                     }
                     else if(L())
                     {
                         return true;
                     }
                     else
                     {
                         return false;
                     }
                 }
                 else
                 {
                     if (value < app.length() && app[value] == '('     )
                     {
                         ++value;
                         if (E())
                         {
                             if (value < app.length() && app[value] == ')'      )
                             {
                                 ++value;
                                 return true;
                             }
                         }
                     }
                 }
                 return false;
             }


             bool U()
             {
                 if(app[value] == '+' || app[value] == '-'  || app[value] == '!')
                 {
                     ++value;
                     return true;
                 }
                 return false;
             }
             

             bool I()
             {
                 if(C())
                 {
                     ++value;
                 }
                 else if(I())
                 {
                     return true;
                 }
                 else
                 {
                     return true;
                 }
                 return false;
             }


             
             bool C()
             {
                 if (value < app.length() && (app[value] >= 'a' && app[value] <= 'z'))
                 {
                     ++value;
                     return true;
                 }
                 return false;
                 
             }

             bool L()
             {
                 if(D())
                 {
                     ++value;
                 }
                 
                 else if(L())
                 {
                     return true;
                 }
                 else
                 {
                     return true;
                 }
                 return false;
             }
             


             bool D()
             {
                 if (value < app.length() && (app[value] >= '0' && app[value] <= '9'))
                 {
                     ++value;
                     return true;
                 }
                 return false;
             }




             
             
             
             
             
             
             
             
             
             



        







         

























   



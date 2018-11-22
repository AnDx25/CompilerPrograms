/*
E->TE'
T->KT'|T'
T'->*KT'|(E)T'|epsilon
E'->+TE'|epsilon
K->a|..|z

*/

	
#include<stdio.h>
#include<ctype.h>
#include<string.h>
 
void Tprime();
void Eprime();
void E();
void check(); 
void T();
 
 
char expression[10];
int count, flag;
 
int main()
{
      count = 0;
      flag = 1;
      printf("\nEnter an Algebraic Expression:\t");
      scanf("%s", expression);
      E();
      if((strlen(expression) == count) && (flag == 0))
      {
            printf("\nThe Expression %s is Valid\n", expression);
      }
      else 
      {
            printf("\nThe Expression %s is Invalid\n", expression);
      }
}
                    
void E()
{printf("E");
      T();
      Eprime();
flag=0;
}
 
void T()
{printf("T");
if(isalnum(expression[count])){
      check();
      Tprime();
}
Tprime();
} 
void Tprime()
{printf("Tprime");
      if(expression[count] == '*')
      {
            count++;
            check();
            Tprime();
      }
if(expression[count] == '(')
      {
            count++;
            E();
            if(expression[count] == ')')
            {
                  count++;
            }
            
     Tprime();
      }       
}
 
void check()
{printf("check");
      if(isalnum(expression[count]))
      {
            count++;
      }  
      else
      {
            flag = 1; //error
      }
}
 
void Eprime()
{printf("Eprime");
      if(expression[count] == '+')
      {
            count++;
            T();
            Eprime();
      }
}

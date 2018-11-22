%{
#include<stdio.h>
int lines=0,words=0,s_ltr=0,c_ltr=0,num=0,specl_char=0,total=0;
%}

%%
[\n] {lines++; words++;}
[\t ' ']  words++;
[A-Z]  c_ltr++;
[a-z]  s_ltr++;
[0-9]  num++;
. specl_char++;
%%


main()
{
yyin=fopen("/home/kshitiz/Desktop/Compilers_Lab/LAB-8/C_lexer/test.txt","r");
yylex();
total=s_ltr+c_ltr+num+specl_char;
printf("The string contains \n\t%d lines\n\tIn total %d characters",lines,total);
fclose(yyin);
}

%%
[ \t]+[c][h][u][t][i][y][a][ ]+[k][a][u][n][ ]+[h][a][i][ ?]+  {printf("Ravi ... aur kaun ...",yytext);}
[\t]+
is  | 
am  | 
are |
was |
were	{printf("%s : is a verb\n",yytext);}
[a-zA-Z]+ {printf("%s : is not a verb ,try again\n",yytext);}

.|\n
%%
main()
{
yylex();
}

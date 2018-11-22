%{
#include<stdio.h>
int vow_count=0;
int con_count=0;
int art=0;
int con_line=0;
int index1=0;
%}
%%
"the"[ \t\n]			{art++;index1++;printf("%s is article at %d\n",yytext,index1);}
"The"[ \t\n]			{art++;index1++;printf("%s is article at %d\n",yytext,index1);}
"a"[ \t\n]			{art++;index1++;printf("%s is article  at %d\n",yytext,index1);}
"an"[ \t\n]			{art++;index1++;printf("%s is article  at %d\n",yytext,index1);}
[0-9][ \t\n]
[a|e|i|o|u|E|A|I|O|U][a-zA-Z]*[ \t\n]	{vow_count++;index1++;printf("%s is vowel  at %d\n",yytext,index1);}
[a-zA-Z(^a|i|e|o|u|E|A|I|O|U)][a-zA-Z]*[ \t\n] {con_count++;index1++; printf("%s is consonant at %d\n",yytext,index1);}
[.|,]						{con_line++;index1++;}

.			;
%%
int main(int param_count ,char **param )
{
	FILE *fp;
	if(param_count==2)
	{
		if (!(fp = fopen(param[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
		yyset_in(fp);

		yylex();
		printf("No of vowels=%d\n",vow_count);
		printf("No of consonant =%d\n",con_count);
		printf("No of articles=%d\n",art);
		printf("No of sentences =%d\n",con_line);
	}
return 0;
}

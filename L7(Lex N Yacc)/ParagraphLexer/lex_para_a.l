%{// yyleng  ==> 1 to (yyleng-1)
#include<stdio.h>
#include<fnmatch.h>
#include<string.h>
FILE *file;
char *vowel[1000],*consonant[1000];
int v_index[1000],c_index[1000];
int sentence=1,numeral=0,freq_articles=0,i=0,j=0,k=0;
//char *abbr="[A-Z][a-z]+[.]";
//char *acro="([A-Z].)+";
%}
spcl_char [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
word [a-zA-Z]+

%%

[^a-zA-z0-9{spcl_char}][aeiouAEIOU][a-z0-9A-Z]+	{
char str[100];
int var;
for(var=1;var<yyleng;var++)
{
str[var-1]=yytext[var];
//printf("\n%c\t%d",yytext[var],var);
}
str[var-1]='\0';
vowel[i]= (char *)malloc(strlen(str)+1);
int index=0;
while(index <= strlen(str))
{
  vowel[i][index] = str[index];
  index++;
}
i++;
}


[^a-zA-z0-9{spcl_char}][^aeiouAEIOU][a-z0-9A-Z]+	{
char str[100];
int var;
for(var=1;var<yyleng;var++)
{
str[var-1]=yytext[var];
//printf("\n%c\t%d",yytext[var],var);
}
str[var-1]='\0';
consonant[j]= (char *)malloc(strlen(str)+1);
int index=0;
while(index <= strlen(str))
{
  consonant[j][index] = str[index];
  index++;
}
j++;
}


[0-9]+	|
[0-9]+\.[0-9]+	{numeral++;}


[ .](a|An)[ ]	|
[ .](an|A)[ ]	|
[ .](the|The)[ ]	{freq_articles++;}

 /* Counting number of sentences*/

       
[ ]+[.][ \n]+	|
[A-Z][a-z][a-z0-9]+[.][ A-Za-z]+	|
[A-Za-z 0-9]+[.][a-z ]+	|
[A-Za-z 0-9]+[.][ A-Z][a-z0-9]+	{sentence++;}



%%

int main()
{
int item=0;
file=fopen("para.txt","r+");
yyin=file;
yylex();
printf("\n|---------------------------------------------------------|");
printf("\n\t\t\tRESULT");
printf("\n|---------------------------------------------------------|");
for(item=0;item<i;item++)
printf("\n\t\t\t%s => vowel[%d]",vowel[item],item);
printf("\n|---------------------------------------------------------|");
for(item=0;item<j;item++)
printf("\n\t\t\t%s => consonant[%d]",consonant[item],item);
printf("\n|---------------------------------------------------------|");
printf("\n\t\t%d Number of numerals",numeral);
printf("\n|---------------------------------------------------------|");
printf("\n\t\t%d number of articles",freq_articles);
printf("\n|---------------------------------------------------------|");
printf("\n\t\t%d sentences",sentence);
printf("\n|---------------------------------------------------------|");
return 0;
}
int yywrap()
{
return 1;
}


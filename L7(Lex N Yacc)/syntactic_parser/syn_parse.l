%{
/*
 * We expand upon the first example by adding recognition of some other
 * parts of speech.
 */

%}
%%

[\t ]+                    /* ignore whitespace */ ;
is |
am |
are |
were |
was |
be |
being |
going |
doing |
walking |
been |
do |
does |
did |
will |
would |
should |
can |
could |
has |
have |
had |
go       { printf("%s: is a verb\n", yytext); }

very |
simply |
gently |
quietly |
calmly |
angrily   { printf("%s: is an adverb\n", yytext); }

to |
from |
behind |
above |
below |
between  { printf("%s: is a preposition\n", yytext); }

if |
then |
and |
but |
or       { printf("%s: is a conjunction\n", yytext); }

their |
my |
your |
his |
her |
its      { printf("%s: is a adjective\n", yytext); }

I |
you |
he |
she  |
we  |
they       { printf("%s: is a pronoun\n", yytext); }


[a-zA-Z]+ {
       printf("%s:  is a noun\n", yytext);
      }
.|\n        { ECHO;/* normal default anyway */ }




%%
int yywrap(void)
{
	return 1;
}
int main()
{
     yylex();
	return 0;
}

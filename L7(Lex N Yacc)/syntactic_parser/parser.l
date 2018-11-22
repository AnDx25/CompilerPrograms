%{
#include "y.tab.h"
%}
%%
is |
am |
are |
were |
was |
be |
being |
going |
goes |
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
go       { return VERB; }

very |
simply |
gently |
quietly |
calmly |
angrily   { return ADVERB; }

to |
from |
behind |
above |
below |
between     { return PREPOSITION; }

if |
then |
and |
but |
or       { return CONJUNCTION; }

their |
my |
your |
his |
her |
its      { return ADJECTIVE; }

I |
you |
he |
she  |
we  |
they       { return PRONOUN ; }

[a-zA-Z]+ {
       return NOUN;
      }

.|\n         ;

%%

int yywrap (void) {return 1;}


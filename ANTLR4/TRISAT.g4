grammar TRISAT;

formula
    : clause ('&&' clause)* #AllClauses
    ;

clause
    : '(' NEGATION? VAR '||' NEGATION? VAR '||' NEGATION? VAR')' #SingleClause
    ;

VAR: [a-zA-Z];

NEGATION: '!';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
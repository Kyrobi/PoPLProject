grammar MyGrammar;

IF: 'if';
THEN: ':';
ELSE: 'else';
ELIF: 'elif';

LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';
EQUAL: '==';
NOT_EQUAL: '!=';

AND: 'and';
OR: 'or';
NOT: 'not';

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MOD: '%';
SET: '=';
PLUS_SET: '+=';
MINUS_SET: '-=';
MULT_SET: '*=';
DIV_SET: '/=';

VAR: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' (ESC | ~["\\])* '"';
WS: [ \t\r\n]+ -> skip;

fragment ESC: '\\' [btnr\\"];
fragment DIGIT: [0-9];


start: statement;
statement: assign_operation | expression | if_statement;

if_statement: IF expression THEN statement (ELIF expression THEN statement)* ELSE THEN statement;

assign_operation: VAR SET expression;

expression: assign_operation | adding_operation | relational_expression;

relational_expression: number LESS_THAN number | number LESS_THAN_OR_EQUAL number | number GREATER_THAN number | number GREATER_THAN_OR_EQUAL number | number EQUAL number | number NOT_EQUAL number;

adding_operation: multiply_operation ( (PLUS | MINUS) multiply_operation)*;

multiply_operation: single_operation ( (MULTIPLY | DIVIDE | MOD) single_operation)*;

single_operation: PLUS number | MINUS number | number;

number: INT | FLOAT | VAR | STRING;

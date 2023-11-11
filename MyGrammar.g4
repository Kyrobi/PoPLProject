grammar MyGrammar;

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
WS: [ \t\r\n]+ -> skip;


start: statement;
statement: assign_operation | expression;

assign_operation: VAR SET expression;

expression: assign_operation | adding_operation;

adding_operation: multiply_operation ( (PLUS | MINUS) multiply_operation)*;

multiply_operation: single_operation ( (MULTIPLY | DIVIDE | MOD) single_operation)*;

single_operation: PLUS number | MINUS number | number;

number: INT | FLOAT | VAR;
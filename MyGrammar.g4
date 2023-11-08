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

start: S;
S: '0' S '0' | '0' S '1' | '1' S '0' | '1' S '1' | '0' | '1';
WS: [ \t\r\n]+ -> skip;

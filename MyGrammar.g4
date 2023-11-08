grammar MyGrammar;
start: S;
S: '0' S '0' | '0' S '1' | '1' S '0' | '1' S '1' | '0' | '1';
WS: [ \t\r\n]+ -> skip;

rm MyGrammar.interp  
rm MyGrammar.tokens  
rm MyGrammarLexer.interp  
rm MyGrammarLexer.py  
rm MyGrammarLexer.tokens  
rm MyGrammarParser.py
sleep 1
antlr4 -Dlanguage=Python3 MyGrammar.g4
sleep 1
python3 makeTree.py
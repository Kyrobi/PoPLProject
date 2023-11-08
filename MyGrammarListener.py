# Generated from MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#start.
    def enterStart(self, ctx:MyGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#start.
    def exitStart(self, ctx:MyGrammarParser.StartContext):
        pass



del MyGrammarParser
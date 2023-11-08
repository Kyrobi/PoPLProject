# Generated from MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,31,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,1,4,1,26,8,1,11,1,
        12,1,27,1,1,1,1,0,0,2,1,1,3,2,1,0,1,3,0,9,10,13,13,32,32,35,0,1,
        1,0,0,0,0,3,1,0,0,0,1,22,1,0,0,0,3,25,1,0,0,0,5,6,5,48,0,0,6,7,3,
        1,0,0,7,8,5,48,0,0,8,23,1,0,0,0,9,10,5,48,0,0,10,11,3,1,0,0,11,12,
        5,49,0,0,12,23,1,0,0,0,13,14,5,49,0,0,14,15,3,1,0,0,15,16,5,48,0,
        0,16,23,1,0,0,0,17,18,5,49,0,0,18,19,3,1,0,0,19,20,5,49,0,0,20,23,
        1,0,0,0,21,23,2,48,49,0,22,5,1,0,0,0,22,9,1,0,0,0,22,13,1,0,0,0,
        22,17,1,0,0,0,22,21,1,0,0,0,23,2,1,0,0,0,24,26,7,0,0,0,25,24,1,0,
        0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,
        6,1,0,0,30,4,1,0,0,0,3,0,22,27,1,6,0,0
    ]

class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    S = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "S", "WS" ]

    ruleNames = [ "S", "WS" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



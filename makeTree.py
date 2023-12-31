# from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from antlr4 import *
from antlr4.tree.Trees import Trees
from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser
from MyGrammarListener import MyGrammarListener


# input_stream = FileStream('input.txt')
# lexer = MyGrammarLexer(input_stream)
# tokens = CommonTokenStream(lexer)
# parser = MyGrammarParser(tokens)
# tree = parser.start()

# listener = MyGrammarListener()
# walker = ParseTreeWalker()
# walker.walk(listener, tree)

input = FileStream('input.txt')
lexer = MyGrammarLexer(input)
stream = CommonTokenStream(lexer)
parser = MyGrammarParser(stream)

listener = MyGrammarListener()
walker = ParseTreeWalker()
tree = parser.start()
print(Trees.toStringTree(tree, None, parser))

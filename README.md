# PoPLProject
Repo for the CMP_SC 4450

# About
This project is a simple demonstration of implementing the Pything 3.x
language using context-free grammar (CFG). The program contains the basics
such as arithmetic operators, assignment operators, if/else blocks, loops, 
and a few others.

This is not meant to be a fully accurate solution, but a demonstration of the knoweldge we've learned in the class and putting it into use.

# Team Members
- Cynwell S.
- Aimen B.

# Requirements 
This program is test on Python 3.10.6. Other versions are not
guaranteed to work. **This program also requires installing pip to download. 
Before installing it make sure your sudo is updated (sudo apt-get update).
Install pip using the command (sudo apt install python3-pip).**

libraries required:
- antlr4 (pip install antlr4-python3-runtime)
- antlr4 (sudo apt-get install antlr4)
- antlr4 tools (pip install antlr4-tools)


# How to use:
1. Clone the files to your local computer.
2. Edit the files with your desired values.
    * 2.1 input.txt is where you will put the expression that you want to generate into a string parse tree.
    * 2.2 MyGrammar.g4 is the file in which you can define your context free grammar (CFG) for the parser.
3. Run ./build.sh to generate all the required files and output the parse tree.

Repeat step 2 and 3 after every changes you make.


# Generating Parse Tree
- If you want to display the result in a parse tree, you'll need to download
the ANTLR4 plugin for IntelliJ and watch this video on how to use it: https://www.youtube.com/watch?v=EDu7Z_F09Lw

# Possible issues
- When trying to ruild the build script after everything has been installed,
it's possible that you get an error similar to "Exception: Could not deserialize
ATN with version  (expected 4). In that case, follow this link: https://stackoverflow.com/questions/76308886/could-not-deserialize-atn-with-version-expected-4-while-using-python-age-drive

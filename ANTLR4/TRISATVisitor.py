# Generated from TRISAT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TRISATParser import TRISATParser
else:
    from TRISATParser import TRISATParser

# This class defines a complete generic visitor for a parse tree produced by TRISATParser.

class TRISATVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TRISATParser#AllClauses.
    def visitAllClauses(self, ctx:TRISATParser.AllClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TRISATParser#SingleClause.
    def visitSingleClause(self, ctx:TRISATParser.SingleClauseContext):
        return self.visitChildren(ctx)



del TRISATParser
from ANTLR4.TRISATParser import *
from ANTLR4.TRISATVisitor import *
from ast import *


class TRISAT_Builder(TRISATVisitor):

    def visitAllClauses(self, ctx: TRISATParser.AllClausesContext):
        clauses = []
        for clause in ctx.clause():
            clauses.append(self.visit(clause))
        return NodeFormula(clauses)

    def visitSingleClause(self, ctx: TRISATParser.SingleClauseContext):
        variables = []
        negation = False
        for char in ctx.getText():
            # Ignore brackets and OR operator.
            if char in ["(", ")", "|"]:
                continue
            # This symbol implies that the complement of the Variable following it was taken.
            elif char == "!":
                negation = True
            # Variable.
            else:
                variables.append(NodeVar(char, negation))
                negation = False
        return NodeClause(variables)

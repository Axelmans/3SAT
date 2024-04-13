from ANTLR4.TRISATVisitor import *
from visitor import *
from SUBSETSUM import *


# Determine all the variable names present in the Formula
def all_vars(node: NodeFormula) -> list:
    formula_vars = []
    for clause in node.clauses:
        for var in clause.vars:
            if var.identifier not in formula_vars:
                formula_vars.append(var.identifier)
    return formula_vars


# Does the assignment of a certain variable fulfill the given clause?
def fulfills(var: str, neg: bool, node: NodeClause) -> bool:
    for var_node in node.vars:
        if var_node.identifier == var and var_node.neg == neg:
            return True
    return False


class TRISAT_SUBSETSUM_Reducer(Visitor):

    # The reduction is explained in reduction.txt
    def visitNodeFormula(self, node: NodeFormula):
        multiset = []
        # The map keeps track of numbers corresponding to variable assignments,
        # used to determine the full satisfying assignment after a SUBSETSUM solution is found.
        # It does not contain information about clauses since it is not very useful for the truth assignment.
        mapped_multiset = {}
        solution = {}
        for i in range(len(node.clauses)):
            multiset += [10 ** i, 10 ** i]
        formula_vars = all_vars(node)
        for i in range(len(formula_vars)):
            nr = 10 ** (len(node.clauses) + i)
            neg_nr = nr
            for j in range(len(node.clauses)):
                if fulfills(formula_vars[i], False, node.clauses[j]):
                    nr += 10 ** j
                if fulfills(formula_vars[i], True, node.clauses[j]):
                    neg_nr += 10 ** j
            multiset += [nr, neg_nr]
            mapped_multiset[nr] = formula_vars[i], True
            mapped_multiset[neg_nr] = formula_vars[i], False
        print("The generated multiset:")
        print(multiset)
        print("This is the sum we must be able to obtain:")
        desired_sum = int("1" * len(formula_vars) + "3" * len(node.clauses))
        print(desired_sum)
        subsetsum_obj = SUBSETSUM(multiset)
        subset = subsetsum_obj.subsetsum(desired_sum)
        if not subset:
            print("No satisfying assignment!")
            return None
        for number in subset:
            if len(str(number)) > len(node.clauses):
                var_assignment = mapped_multiset[number]
                solution[var_assignment[0]] = var_assignment[1]
        print("Satisfying assignment found!")
        print(solution)
        return solution

    def visitNodeClause(self, node: NodeClause):
        pass

    def visitNodeVar(self, node: NodeVar):
        pass

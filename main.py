from TRISAT_builder import *
from TRISAT_SUBSETSUM_reducer import *
from ANTLR4.TRISATLexer import TRISATLexer, InputStream, CommonTokenStream


lexer = TRISATLexer(InputStream(open("test.txt", "r").read()))
stream = CommonTokenStream(lexer)
parser = TRISATParser(stream)
tree = parser.formula()
builder = TRISAT_Builder()
ast = builder.visit(tree)
subsetsum_reducer = TRISAT_SUBSETSUM_Reducer()
subset = ast.accept(subsetsum_reducer)
fei = "fei"

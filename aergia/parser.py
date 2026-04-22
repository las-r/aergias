from .nodes import *

# aergia parser
# made by las-r on github

# expression parser
def parseexpr(tokens):
    if not tokens:
        return None
    token = tokens.pop(0)
    
    # if/while blocks
    if token == "(":
        cond = parseexpr(tokens)
        body = []
        while tokens and tokens[0] != ")":
            body.append(parseexpr(tokens))
        if tokens: tokens.pop(0)
        elsebody = []
        if tokens and tokens[0] == "(":
            tokens.pop(0)
            while tokens and tokens[0] != ")":
                elsebody.append(parseexpr(tokens))
        return IfNode(cond, body, elsebody)
    
    if token == "[":
        cond = parseexpr(tokens)
        body = []
        while tokens and tokens[0] != "]":
            body.append(parseexpr(tokens))
        if tokens: tokens.pop(0)
        return WhileNode(cond, body)
    
    # assignments
    if token == "=":
        name = tokens.pop(0)
        value = parseexpr(tokens)
        return AssignNode(name, value)
    
    # binary ops
    if token in ("+", "-", "*", "/", "==", "!=", ">>", "<<", ">=", "<=", "^", "%", "&", "|", "$"):
        left = parseexpr(tokens)
        right = parseexpr(tokens)
        return BinaryOpNode(token, left, right)
    
    # unary ops and output
    if token in ("!", "~", ">"):
        child = parseexpr(tokens)
        if token == ">": return OutputNode(child)
        return UnaryOpNode(token, child)
    
    # input
    if token == ".": return IntInputNode()
    if token == ",": return StringInputNode()
    if token == "'": return FloatInputNode()
    
    # string
    if token.startswith('"'): return LiteralNode(token.strip('"'))
    
    # number and variable
    try:
        val = float(token)
        return LiteralNode(int(val) if val.is_integer() else val)
    except ValueError:
        return VariableNode(token)

# tree maker
def parse(tokens):
    ast = []
    while tokens:
        node = parseexpr(tokens)
        if node:
            ast.append(node)
    return ast
# https://gist.github.com/Zirak/6341918

# create dictionary of dictionaries
operators = {
    # addition
    '+' : {
        'prec' : 1,
        'calc' : lambda a,b: a + b },
    # subtraction
    '-' : {
        'prec' : 1,
        'calc' : lambda a,b: a - b },
    # multiplication
    '*' : {
        'prec' : 2,
        'calc' : lambda a,b: a * b },
    # division
    '/' : {
        'prec' : 2,
        'calc' : lambda a,b: a / b },
    # exponentiation
    '^' : {
        'prec' : 3,
        'assoc' : 'right',
        'calc' : lambda a,b: a ** b },
        }

# add symbol to all dict entries
for key in operators:
    operators[key]['symbol'] = key

class Calculator:
    def __init__ (self):
        self.operators = operators
 
    def calc (self, inp):
        self.parse(inp)
        self.ast = self.to_ast()
        return self.ast.calc() if self.ast is not None else None
 
    def parse (self, inp):
        tokens = list(inp.replace(' ', '')) #no, this is terrible. You can't differentiate two-digit numbers
        self.opstack = []
        self.out = []
 
        while tokens:
            self.parse_token(tokens.pop(0))
 
        while self.opstack:
            self.out.append(self.opstack.pop())

    def parse_token (self, tok):
        if is_number(tok):
            self.out.append(NumberToken(tok))
        elif self.operators.has_key(tok):
            actual_tok = OperatorToken(self.operators[tok])
            self.parse_op(actual_tok)
        #add parentheses handling
        else:
            raise SyntaxError('Unrecognized token ' + str(tok));

def is_number (string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class Token:
    pass

class NumberToken(Token):
    def __init__ (self, val):
        self.value = float(val) if '.' in str(val) else int(val)
 
    def calc (self):
        return self.value
 
    def humane_str (self):
        return str(self)
 
    def __str__ (self):
        return str(self.value)
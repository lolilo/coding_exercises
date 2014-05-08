import re
num_pattern = re.compile('[0-9]+')
op_pattern = re.compile('[*+-/]')
paren_pattern = re.compile('[()]')

# PRECEDENCE = {
#     '+': 1,
#     '-': 1,
#     '/': 2,
#     '*': 2
# }

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2

def parse(user_input):
    tokens = user_input.split()
    return tokens

def create_out_queue(user_input):
    tokens = parse(user_input)

    out_queue = []
    op_stack = []

    while tokens:
        token = tokens.pop(0)
        if num_pattern.match(token):
            out_queue.append(token)
        elif op_pattern.match(token):
            if not op_stack or precedence(op_stack[-1]) < precedence(token):
                op_stack.append(token)
            elif precedence(op_stack[-1]) >= precedence(token):
                to_queue = op_stack.pop()
                out_queue.append(to_queue)
                op_stack.append(token)
            else: 
                print "WHAT IS THIS.", token
        else:
            print "Unexpected token %r" %token
    # output to reverse polish notation/RPN
    while op_stack:
        operator = op_stack.pop()
        out_queue.append(operator)
    print out_queue
    return out_queue

def create_ast(user_input):
    tokens = parse(user_input)

    out_queue = [] # list of expressions in the form of lists -- a single expression grouped into a list
    op_stack = []

    while tokens: 
        token = tokens.pop(0)
        if num_pattern.match(token):
            out_queue.append(token)
        elif op_pattern.match(token):
            if not op_stack or precedence(op_stack[-1]) < precedence(token):
                op_stack.append(token)
            elif precedence(op_stack[-1]) >= precedence(token):
                operator = op_stack.pop()
                # group together an expression
                arg2 = out_queue.pop(-1)
                arg1 = out_queue.pop(-1)
                out_queue.append([arg1, arg2, operator])

                op_stack.append(token)
            else: 
                print 'this should not print ever'
        else:
            print "Unexpected token %r" %token

    # finished traversing through all tokens; complete out_queue
    while op_stack:
        operator = op_stack.pop(-1)
        arg2 = out_queue.pop(-1)
        arg1 = out_queue.pop(-1)
        out_queue.append([arg1, arg2, operator])
    # print out_queue
    return out_queue

# takes in an ast in the form of a list and outputs a string of the expression 
# in postfix notation
def ast_to_postfix(ast):
    if not ast:
        return 
    if len(ast) == 1: # a single number as a string
        return ast
    operator = ast[-1]
    arg1 = ast[-3]
    arg2 = ast[-2]

    return '(' + ast_to_postfix(arg1) + ' ' + ast_to_postfix(arg2) + ' ' + operator + ')'

def infix_to_postfix(user_input):
    ast = create_ast(user_input)[0]
    print 'ast is', ast
    return ast_to_postfix(ast)

s = '3 * 4 - 2'
print infix_to_postfix(s)

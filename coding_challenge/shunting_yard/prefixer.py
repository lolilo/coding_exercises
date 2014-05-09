import re, sys
from os.path import exists
import operator as op

NUM_PATTERN = re.compile('[0-9]+')
ALPHA_PATTERN = re.compile('[a-zA-Z]')
OP_PATTERN = re.compile('[*+-/]')

PRECEDENCE = {
    '+': 1,
    '-': 1,
    '/': 2,
    '*': 2,
    '(': 0
}

EXECUTE = { 
    '+' : op.add, 
    '-' : op.sub, 
    '*' : op.mul, 
    '/' : op.div, 
}

def parse(user_input):
    tokens = user_input.split()
    return tokens

def create_ast(user_input):
    tokens = parse(user_input)

    out_queue = [] # list of expressions in the form of lists -- a single expression grouped into a list
    op_stack = []

    while tokens: 
        token = tokens.pop(0)
        # number or alphabetic character
        if NUM_PATTERN.match(token) or ALPHA_PATTERN.match(token):
            out_queue.append(token)
        # operator
        elif OP_PATTERN.match(token):
            token_precedence = PRECEDENCE[token]
            if not op_stack or PRECEDENCE[op_stack[-1]] < token_precedence:
                op_stack.append(token)

            # a non-empty stack exists; check precedence of top of stack
            elif PRECEDENCE[op_stack[-1]] >= token_precedence:
                # group together an expression
                operator = op_stack.pop()
                arg2 = out_queue.pop(-1)
                arg1 = out_queue.pop(-1)
                out_queue.append([arg1, arg2, operator])
                # append new operator to stack
                op_stack.append(token)
            else: 
                print 'this should not print ever'

        # left parenthesis
        elif token == '(':
            op_stack.append(token)

        # right parenthesis
        elif token == ')':
            next = op_stack.pop(-1)
            while next != '(':
                arg2 = out_queue.pop(-1)
                arg1 = out_queue.pop(-1)
                out_queue.append([arg1, arg2, next])   
                next = op_stack.pop(-1)     
            # when we find '(', simply discard, don't do anything with 'next' at this point

        else:
            print "Unexpected token %r" %token

    # finished traversing through all tokens; complete out_queue
    while op_stack:
        operator = op_stack.pop(-1)
        arg2 = out_queue.pop(-1)
        arg1 = out_queue.pop(-1)
        out_queue.append([arg1, arg2, operator])
    return out_queue

# takes in an ast in the form of a list and outputs a string of the expression 
# in postfix notation
def ast_to_postfix(ast):
    if len(ast) == 1: # a single number as a string
        return ast
    operator = ast[-1]
    arg1 = ast_to_postfix(ast[-3])
    arg2 = ast_to_postfix(ast[-2])
    return '(' + arg1 + ' ' + arg2 + ' ' + operator + ')'

def infix_to_postfix(user_input):
    ast = create_ast(user_input)[0]
    return ast_to_postfix(ast)

# returns an int if input string is num, otherwise returns input string
def num_string_to_int(s):
    if NUM_PATTERN.match(s):
        return int(s)
    else: 
        return s

def evaluate_ast(ast):
    if len(ast) == 1:
        if NUM_PATTERN.match(ast):
            return int(ast)
        if ALPHA_PATTERN.match(ast):
            return ast
    else:
        operator = ast[-1]
        arg1 = evaluate_ast(ast[-3])
        arg2 = evaluate_ast(ast[-2])
        if type(arg1) == type(arg2) == int:
            return EXECUTE[operator](arg1, arg2)
        else: 
            return '(' + str(arg1) + ' ' + str(arg2) + ' ' + operator + ')'

def evaluate_expression(user_input):
    ast = create_ast(user_input)[0]
    return evaluate_ast(ast)   

def read_in_file_from_commandline():
    # could also use arg parse or opt parse python module

    args = sys.argv # obtain list of args from commandline
    r_flag = False
    proper_setup = True
    while args:
        arg = args.pop(0)
        if arg == '-r':
            r_flag = True
        else:
            # this first be incorrectly assigned to prefixer.py, 
            # but later replaced with the proper filename
            if exists(arg):
                infix_file = arg
            else: 
                proper_setup = False
                print '%r does not exist!' % arg 

    if proper_setup:
        print infix_file
        infix_file = open(infix_file)
        expression = infix_file.readline().strip()

        if r_flag: 
            print evaluate_expression(expression)
        else: 
            print infix_to_postfix(expression)

def main():
    read_in_file_from_commandline()

if __name__ == "__main__":
    main()

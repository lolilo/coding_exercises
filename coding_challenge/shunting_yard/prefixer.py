import re
num_pattern = re.compile('[0-9]+')
op_pattern = re.compile('[*+-/%]')

def parse(user_input):
    tokens = user_input.split()
    return tokens

def create_out_queue(user_input):
    tokens = parse(user_input)

    out_queue = []
    op_stack = []
    # postfix = ''

    while tokens:
        token = tokens.pop(0)
        if num_pattern.match(token): #this breaks...passes for 6+5 -- still matches 6. need to ensure tokens do not mix op and num
            out_queue.append(token)
        elif op_pattern.match(token):
            op_stack.append(token)
        else:
            print "Unexpected token %r" %token
    # output to reverse polish notation/RPN
    while op_stack:
        operator = op_stack.pop()
        out_queue.append(operator)
    return out_queue

def infix_to_postfix(user_input):
    out_queue = create_out_queue(user_input)
    return out_string(out_queue)

# recursively traverse out_queue
def out_string(queue):
    if len(queue) == 3:
        operator = queue[2]
        arg1 = queue[0]
        arg2 = queue[1]
        return '(' + arg1 + ' ' + arg2 + ' ' + operator + ')'
    operator = queue[-1]
    arg1 = queue[0]
    arg2 = out_string(queue[1:-1])
    return '(' + arg1 + ' ' + arg2 + ' ' + operator + ')'

s = '3 + 4 * 2'

print infix_to_postfix(s)
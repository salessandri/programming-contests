#!/usr/bin/python

from collections import deque

symbols = set(['+', '-', '*', '/', '^'])

def to_rpn(string):
    global symbols
    
    operand_stack = []
    symbol_stack = []
    for c in string:
        if c == '(':
            operand_stack.append('(')
            symbol_stack.append('(')
        elif c == ')':
            new_op_stack = []
            while operand_stack[-1] != '(':
                new_op_stack.insert(0, operand_stack.pop())
            operand_stack.pop()
            new_sy_stack = []
            while symbol_stack[-1] != '(':
                new_sy_stack.insert(0, symbol_stack.pop())
            symbol_stack.pop()
            operand_stack.append(solve_stacks(new_op_stack, new_sy_stack))
        elif c in symbols:
            symbol_stack.append(c)
        else:
            operand_stack.append(c)
    
    return solve_stacks(operand_stack, symbol_stack)

def solve_stacks(operand_stack, symbol_stack):
    while len(operand_stack) > 1:
        if '^' in symbol_stack:
            symb = '^'
        elif '/' in symbol_stack:
            symb = '/'
        elif '*' in symbol_stack:
            symb = '*'
        elif '-' in symbol_stack:
            symb = '-'
        elif '+' in symbol_stack:
            symb = '+'
        
        ind = symbol_stack.index(symb)
        
        new_operand = operand_stack.pop(ind) + operand_stack.pop(ind) + symbol_stack.pop(ind)
        operand_stack.insert(ind, new_operand)
    return operand_stack[0]

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        print to_rpn(raw_input())


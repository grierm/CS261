# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    parenthesis = ["(", ")"]
    braces = ["{", "}"]
    brackets = ["[", "]"]
    # initialize an empty list as the stack
    stack = []

    reverse_stack = []
    # iterate over each character in the string
    # FIXME: You will write this function ok i will
    for i in input_string:
        if i not in alphabet:
            stack.append(i)
    reverse_stack = stack[::-1]
    is_balanced = True
    i = 0
    for item in stack:
        if item in parenthesis:
            if item == parenthesis[0]:
                if reverse_stack[i] != parenthesis[1]:
                    is_balanced = False
            elif item == parenthesis[1]:
                if reverse_stack[i] != parenthesis[0]:
                    is_balanced = False
        if item in braces:
            if item == braces[0]:
                if reverse_stack[i] != braces[1]:
                    is_balanced = False
            elif item == braces[1]:
                if reverse_stack[i] != braces[0]:
                    is_balanced = False
        if item in brackets:
            if item == brackets[0]:
                if reverse_stack[i] != brackets[1]:
                    is_balanced = False
            elif item == brackets[1]:
                if reverse_stack[i] != brackets[0]:
                    is_balanced = False
        i += 1
    return is_balanced


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))


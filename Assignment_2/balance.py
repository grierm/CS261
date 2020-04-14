# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):
    """
    This will check if the input_string has matching opening and closing symbols,
    which would make it balanced.
    :param input_string: String to be checked.
    :return: True or False depending if it is balanced or not.
    """

    # Set opening and closing symbols
    open_symbols = ["(", "[", "{"]
    close_symbols = [")", "]", "}"]

    # initialize an empty list as the stack
    stack = []

    # initializes balanced to False
    balanced = False

    # If the string is empty, it will be considered balanced
    if input_string == "":
        balanced = True

    # Iterates through every symbol in the input_string
    # FIXME: You will write this function
    for symbol in input_string:

        # Add an open symbol to the stack
        if symbol in open_symbols:
            stack.append(symbol)

        # If it's a closing symbol, checks if it's a match, then removes it from the stack
        elif symbol in close_symbols:
            position = close_symbols.index(symbol)
            if len(stack) > 0 and open_symbols[position] == stack[len(stack) - 1]:
                stack.pop()

        # If all opening symbols had a correctly positioned closing symbol,
        # the length of the stack is 0, which means it's balanced
        if len(stack) == 0:
            balanced = True

    return balanced

if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))


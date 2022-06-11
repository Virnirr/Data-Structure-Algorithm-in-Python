from re import S
from stack_array import Stack

# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str: str) -> float:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""

    # split string into an array
    rpn_expression = input_str.split()

    # operators
    opt = ["-", "+", "*", "/", "//", "**", "<<", ">>"]

    # creating a Stack 
    operand_stack = Stack(30)

    for i in rpn_expression:

        try:
            if i in opt:
                pass
            else:
                try:
                    operand_stack.push(int(i))
                except:
                    operand_stack.push(float(i))
        except:
            raise PostfixFormatException("Invalid token")
            

        # when operator is encountered, pop last two stack and do math and push back result
        if i in opt:
            if operand_stack.size() < 2:
               raise PostfixFormatException("Insufficient operands")

            # instantiating variables
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            # check if there are any ValueErrors when doing math
            # i.e. 0/0 or 2/0 

            # doing math operations
            if i == "-":
                result = operand1 - operand2
            if i == "+":
                result = operand1 + operand2
            if i == "*":
                result = operand1 * operand2
            if i == "/":
                try:
                    result = operand1 / operand2
                except:
                    raise ZeroDivisionError
            if i == "//":
                try:
                    result = operand1 // operand2
                except:
                    raise ZeroDivisionError
            if i == "**":
                result = operand1 ** operand2
            if i == "<<":
                try:
                    result = operand1 << operand2
                except:
                    raise PostfixFormatException("Illegal bit shift operand")
            if i == ">>":
                try:
                    result = operand1 >> operand2
                except:
                    raise PostfixFormatException("Illegal bit shift operand")
            operand_stack.push(result)

    
    # riase error if there are too mayn operands in stack when you finish evaluating all the operators
    if operand_stack.size() >= 2:
        raise PostfixFormatException("Too many operands")

    # raise error if there are less than 2 evaluation inputs
    # i.e. "", "1", "2", etc.
    if len(rpn_expression) == 0:
        raise PostfixFormatException("Insufficient operands")

    return operand_stack.peek()


def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """

    # process string from left to right and store it into a list
    split_expression = input_str.split()

    # postfix expression that will be returned at the end of the function call
    rpn_expression = []

    # creating an operator stack
    optstack = Stack(30)

    # operators
    opt = {
        "-": 1,
        "+": 1,
        "*": 2,
        "/": 2,
        "//": 2,
        "**": 3,
        "<<": 4,
        ">>": 4
    }

    # counter to check for the length of the iteration 
    counter = 0
    
    # check for every values in your list
    for i in split_expression:

        counter+=1
        
        # check if the inputs or the tokens are valid or not
        # Invalid if token is neither an operator, parenthesis, or operand

        # Example: checking for anything other than ( ), operators, or operands 
        # like special characters ($, #, @, !, &, ^)
        try:
            if i in list(opt.keys()) or i in "( )":
                pass
            elif type(float(i)) == float:
                rpn_expression.append(i)

        except:
            raise PostfixFormatException("Invalid token")

        # check for open parentheses 
        if i == "(":
            optstack.push(i)

        # check for closed parentheses
        if i == ")":

            while optstack.peek() != "(":
                rpn_expression.append(optstack.pop())

            optstack.pop()
        
        # check for operators in your list
        if i in "- + * / // ** << >>":
            
            # if o1is left-associative and its precedence is less than or equal to that of o2, or 
            # o1 is right-associative, and has precedence less than that of o2 
            while not optstack.is_empty() and (optstack.peek() != "(") and ((i != "**" and opt[i] <= opt[optstack.peek()]) or (opt[i] < opt[optstack.peek()] and i == "**")):
                rpn_expression.append(optstack.pop())

            optstack.push(i)

        # lastly check if the current value is the length fo the split_expression
        # if it is, then add everything in stack or the rest of the operators onto the rpn_expression
        if counter == len(split_expression):
            while not optstack.is_empty():
                rpn_expression.append(optstack.pop())

    # finally connect all the rpn_expression and return a string delimited by space
    return " ".join(rpn_expression)


def prefix_to_postfix(input_str: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    
    # split string into a list
    split_expression = input_str.split()[::-1]
    print(split_expression)

    # operators
    opt = ["-", "+", "*", "/", "//", "**", "<<", ">>"]

    # creating an operator stack
    optstack = Stack(30)

    for i in split_expression:

        # check if the inputs or the tokens are valid or not
        # Invalid if token is neither an operator, parenthesis, or operand
        try:
            if i in opt:
                op1 = optstack.pop()
                op2 = optstack.pop()

                result = op1 + " " + op2 + " " + i
                optstack.push(result)
                continue

            if type(float(i)) == float:
                optstack.push(i)

        except:
            raise PostfixFormatException("Invalid token") 

    # return the final string in the stack, which is the postfix expression
    return optstack.peek()
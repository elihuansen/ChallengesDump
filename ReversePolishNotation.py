# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, 
#     since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.

def reverse_polish_notation(tokens):
    stack = []

    for token in tokens:
        if isinstance(token, int):
            stack.append(token)

        else:
            operator = token
            second_operand = stack.pop()
            first_operand  = stack.pop()

            result = perform(operator, first_operand, second_operand)
        
            stack.append(result)

    return result

def perform(operation, num1, num2):

    def exp(x, y):
        return x ** y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    return {
        '**': exp,
        '*': mul,
        '/': div,
        '+': add,
        '-': sub
    }[operation](num1, num2)
            

if __name__ == '__main__':

    from GradingPrinter import GradingPrinter

    tests = [
      # (IN, OUT)
        ([5, 3, '+'], 8),
        ([3, 2, '*', 11, '-'], -5),
        ([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'], 5),
        ([5, 2, 3, '**', '+', 5, 8, '+'], 13),
        ([6, 3, '-', 2, '**', 11, '-'], -2),
    ]

    grader = GradingPrinter()

    for test_in, expected_output in tests:
        actual_output = reverse_polish_notation(test_in)
        
        grader += (expected_output, actual_output)

    grader.print()
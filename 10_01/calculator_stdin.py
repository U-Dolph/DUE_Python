import sys
import secret_logic


def print_usage():
    print("Usage: <OPERAND> <OPERATOR> <OPERAND>")


def process_one_row(row):
    arguments = row.split()

    if len(arguments) != 3:
        print_usage()

    if not secret_logic.is_numeric(arguments[0]):
        print_usage()

    _op1 = int(arguments[0])

    if not secret_logic.is_supported_operator(arguments[1]):
        print_usage()

    _operator = arguments[1]

    if not secret_logic.is_numeric(arguments[2]):
        print_usage()

    _op2 = int(arguments[2])

    return _op1, _operator, _op2


def get_inputs():
    for row in sys.stdin:
        operand1, operator, operand2 = process_one_row(row)
        result = secret_logic.calculate(operand1, operator, operand2)

        print("result: {}".format(result))


get_inputs()

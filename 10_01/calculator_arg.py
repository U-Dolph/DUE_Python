import sys
import secret_logic


def print_usage():
    print("Usage: <OPERAND> <OPERATOR> <OPERAND>")
    exit(-1)


def get_input():
    if len(sys.argv) != 4:
        print_usage()

    if not secret_logic.is_numeric(sys.argv[1]):
        print_usage()

    _op1 = int(sys.argv[1])

    if not secret_logic.is_supported_operator(sys.argv[2]):
        print_usage()

    _operator = sys.argv[2]

    if not secret_logic.is_numeric(sys.argv[3]):
        print_usage()

    _op2 = int(sys.argv[3])

    return _op1, _operator, _op2


op1, operator, op2 = get_input()
result = secret_logic.calculate(op1, operator, op2)
print("result: {}".format(result))

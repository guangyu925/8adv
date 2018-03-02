#!/var/bin/env python3

import operator
import logging
import sys

class Colors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

operators = {
    '+': operator.add,
    '-': operator.sub,
}

def colorful(number):
    output = Colors.BOLD + str(number) + Colors.END
    if not number < 0:
        return Colors.YELLOW + output
    else:
        return Colors.RED + output

def calculate(arg):
    stack = list()
    inputs = ""
    for token in arg.split():
        if token == '100':
            print("it's 100")
        try:
            value = int(token)
            inputs += Colors.UNDERLINE + Colors.CYAN + token + Colors.END + " "
            stack.append(value)
        except ValueError:
            logging.debug("Current stack: " + str(stack))
            logging.debug("Operator: " + token)
            inputs += Colors.BOLD + Colors.RED + token + Colors.END + " "
            function = operators[token]
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    print("You entered: " + inputs)
    return stack.pop()
 

def main():
    if len(sys.argv) > 1 and str(sys.argv[1]).lower() == 'debug':
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    while True:
        output = calculate(input('rpn calc> '))
        print(Colors.BOLD + colorful(output) + Colors.END)

if __name__ == '__main__':
    main()

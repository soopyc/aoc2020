import sys

import colorama

colorama.init(autoreset=True)

if sys.argv[1] == '':
    print('Solver for day 1')
    print('\nUsage:')
    print(f'    python {sys.argv[0]} [input file]')
    print('\nlogs and output will be printed on stdout.')
    sys.exit(0)

try:
    file = open(sys.argv[1], 'r')
except FileNotFoundError:
    print(colorama.Fore.RED + 'ERROR: file does not exist.' )
    sys.exit(1)

print('wip')


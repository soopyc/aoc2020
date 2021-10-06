import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 1a')

helptext = f"""Usage: python3 {sys.argv[0]} [file]

Required parameters:
    file: input file
"""


def _help(): 
    print(helptext)

if len(sys.argv) == 1:
    utils.warn('no input file specified.')
    _help()
    sys.exit(0)

try:
    with open(sys.argv[1], 'r') as file:
        utils.debug('reading file')
        puzzle = file.read()
except FileNotFoundError:
    utils.error(f'file "{sys.argv[1]}" does not exist.')
    _help()
    sys.exit(1)

utils.debug('splitting stuff')
entries = puzzle.splitlines()
utils.debug(f'{len(entries)} entries')

for i in entries:
    i = int(i)
    for b in entries:
        b = int(b)
        utils.debug(f'checking if {i}+{b} == 2020 ...', end='')
        if i + b != 2020:
            print(f'no ({i+b})')
        else:
            print(f'yes ({i+b})')
            utils.success(f'The values are {i} and {b}, i+b={i+b};i*b={i*b}',
                          text="FOUND")
            sys.exit(0)


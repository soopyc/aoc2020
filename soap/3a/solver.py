
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 3a')

helptext = f'''Usage: python3 {sys.argv[0]} [file]

Required parameters:
    file: input file
'''


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


utils.debug('setting up map')
_map = puzzle.splitlines()

x = 0
trees = 0
ok = 0
for c, level in enumerate(_map):
    if c == 0:
        continue
    x += 3 
    location = x % len(level)
    if level[location] == "#":
        #tree = level[location]
        utils.warn(level, end='\n', text="TREE")
        trees += 1
    else:
        utils.success(level, end='\n', text=" OK ")
        ok += 1

print()
utils.info(f'Traversed map \n\tTrees: {trees}\n\tOkays: {ok}', end='\n')


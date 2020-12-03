
import sys
import json

sys.path.extend(['../'])
import utils

utils.info('Solver for day 3b')

helptext = f'''Usage: python3 {sys.argv[0]} [file] [ruleset]

Required parameters:
    file: input file
 ruleset: ruleset json file
'''


def _help():
    print(helptext)

if len(sys.argv) != 3:
    utils.warn('no input file/too many argument specified.')
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

try:
    with open(sys.argv[2], 'r') as file:
        utils.debug('reading file')
        ruleset = json.load(file)
except FileNotFoundError:
    utils.error(f'file "{sys.argv[1]}" does not exist.')
    _help()
    sys.exit(1)

utils.debug('setting up map')
_map = puzzle.splitlines()

def run(mx, my):
    utils.debug('run called')
    x, y = 0, 0
    trees = 0
    ok = 0
    c = 0
    
    try:
        while True:
            if c == 0:
                c += 1
                continue
            c += 1
            x += mx
            y += my
            level = _map[y]
            location = x % len(level)
            if level[location] == "#":
                #tree = level[location]
                utils.warn(level, end='\n', text="TREE")
                trees += 1
            else:
                utils.success(level, end='\n', text=" OK ")
                ok += 1
    except IndexError:
        pass
    return trees, ok


utils.debug('start iterating rulesets')
ttrees = 0
tok = 0
ttrees_arr = []
for i in ruleset['']:
    _t, _o = run(i[0], i[1])
    ttrees_arr.append(_t if _t != 0 else 1)
    ttrees += _t
    tok += _o

res = 1
utils.debug(ttrees_arr)
for i in ttrees_arr:
    res *= i

print()
utils.info(f'Ran map \n\tTrees: {ttrees}\n\tOkays: {tok}\n\tPart2: {res}',
           end='\n')


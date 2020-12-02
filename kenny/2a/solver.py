
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 2a')

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

success = 0
fail= 0

try:
    with open(sys.argv[1], 'r') as file:
        utils.debug('reading file')
        puzzle = file.read()
except FileNotFoundError:
    utils.error(f'file "{sys.argv[1]}" does not exist.')
    _help()
    sys.exit(1)

entries = puzzle.splitlines()
utils.debug(f'{len(entries)} entries')

for i in entries:
    criteria, character, password = i.split()
    ranges = (int(criteria.split('-')[0]), int(criteria.split('-')[1])+1)
    criteria = range(*ranges)
    character = character.split(':')[0]
    
    counter = 0
    for i in password:
        if i == character:
            counter += 1

    if counter in criteria:
        utils.success(f'Password {password} matches criteria', text=" MATCH ", 
                      end='\n')
        success += 1
    else:
        utils.error(f"Password {password} does not match criteria",
                    text="NOMATCH", end='\n')
        fail += 1


utils.info('Tests finished:')
utils.info(f'- {success} passwords passed')
utils.info(f'- {fail} passwords failed')


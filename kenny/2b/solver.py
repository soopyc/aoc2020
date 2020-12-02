
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 2b')

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
    positions = (int(criteria.split('-')[0])-1, int(criteria.split('-')[1])-1)
    character = character.split(':')[0]

#    try:
#        match = (password[positions[0]] == character) ^ \
#            (password[positions[1]] == character)
#    except IndexError:
#        utils.error(f"Password {password} does not match criteria",
#                    text="NOMATCH", end='\n')
#        fail += 1
#        continue
    match = (password[positions[0]] == character) ^ \
            (password[positions[1]] == character)
    if match:
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


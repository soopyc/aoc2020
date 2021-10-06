
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 4a')

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

required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()

#required_dict = {}
#for i in required_fields:
#    required_dict[i] = 0

utils.debug('prepping passport data')
passports = puzzle.split('\n\n')
successes = 0
fails = 0
for c, i in enumerate(passports):
    #cpass = required_dict.copy()
    passq = True
    passpt = i.replace('\n', ' ')
    for field in required_fields:
        if f'{field:}' not in i:
            utils.error(f'Passport #{c} doesn\'t pass check', text='FAIL')
            passq = False
            fails += 1
            break
    if passq:
        successes += 1
        utils.success(f'Passport #{c} pass checks', text='PASS')

utils.info(f'pass: {successes}\nfail: {fails}')


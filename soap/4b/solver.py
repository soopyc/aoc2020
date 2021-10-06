
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

#required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()


utils.debug('prepping passport data')
puzzle = puzzle.strip()
passports = puzzle.split('\n\n')
[utils.info(f'port: {i}', end='\n') for i in passports]
successes = 0
fails = 0
for c, i in enumerate(passports):
    #cpass = required_dict.copy()
    def check_height(val):
        if val[-2:] == 'cm':
            return int(val[:-2]) in range(150, 194)
        elif val[-2:] == 'in':
            return int(val[:-2]) in range(59, 77)

    def check_hair(val):
        import re
        m = re.match(r'#(([a-f]|\d){6})', val)
        if m:
            return True
        else:
            return False

    passq = True
    seperated = i.replace('\n', ' ')
    seperated = seperated.split(' ')
    try:
        print(seperated)
        keys = dict([i.split(':') for i in seperated])
        assert int(keys['byr']) in range(1920, 2003), 'birth'
        assert int(keys['iyr']) in range(2010, 2021), 'issue'
        assert int(keys['eyr']) in range(2020, 2031), 'expire'
        assert check_height(keys['hgt']), 'height'
        assert check_hair(keys['hcl']), 'hair'
        assert keys['ecl'] in 'amb blu brn gry grn hzl oth'.split(), 'eye'
        assert len(keys['pid']) == 9, 'pid'
    except AssertionError as e:
        utils.error(f'Passport A{c} failed check: {e}', text="FAIL")
        fails += 1
    except KeyError:
        utils.error(f'passport K{c} failed check: no key', text="FAIL")
        fails += 1
    except ValueError:
        utils.error(f'passport V{c} failed check: no value', text="FAIL")
        fails += 1
    else:
        successes += 1
        utils.success(f'Passport #{c} pass checks', text='PASS')

utils.info(f'pass: {successes}\nfail: {fails}')


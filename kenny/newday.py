import sys
import os
import stat

import utils

utils.info('Setting things up')

dirname = utils.question('Enter day and part number (e.g. 1a)')

utils.debug(f'checking if ./{dirname} exists... ', end='')
if os.path.exists(dirname):
    print('yes')
    utils.error(f"{dirname} exists. Please select another "
                f"directory(another day).")
    sys.exit(1)

print('no')
os.mkdir(dirname)
utils.debug(f'created directory {dirname}')

template = f"""
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 1a')

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
    utils.error(f'file "{{sys.argv[1]}}" does not exist.')
    _help()
    sys.exit(1)

"""
utils.debug("templating solver.py")
file = open(os.path.join(dirname, 'solver.py'), 'w+')
file.write(template)
file.close()

utils.debug('creating importer')
importer = "pbpaste > input"
file = open(os.path.join(dirname, 'import_input'), 'w+')
file.write(importer)
file.close()
utils.debug('setting importer permissions')
os.chmod(os.path.join(dirname, 'import_input'), stat.S_IRUSR |
            stat.S_IWUSR | 
            stat.S_IXUSR | 
            stat.S_IRGRP |
            stat.S_IWGRP | 
            stat.S_IXGRP | 
            stat.S_IROTH | 
            stat.S_IWOTH |
            stat.S_IXOTH
        )

utils.success(f"Successfully created new files for day {dirname}")


import sys
import os

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

template = f"""import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day {dirname}')
"""

file = open(os.path.join(dirname, 'solver.py'), 'w+')
file.write(template)
file.close()

utils.success(f"Successfully created new files for day {dirname}")


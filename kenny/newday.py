import utils 
import sys
import os

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



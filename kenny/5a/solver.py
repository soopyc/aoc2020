
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 5a')

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

START_ROW_RANGE = list(range(128))
START_COLUMN_RANGE = list(range(8))


class Ranges:
    def __init__(ranges):
        self._range = ranges

    def f():
        return Ranges(self._range[:len(self._range)//2])

    def b():
        return Ranges(self._range[len(self._range)//2:])


class Seat:
    def __init__(encoded):
        self.encoded = encoded
        self.column = 0
        self.row = 0
        self.parse()

    def parse(self):
        crow = Ranges(START_ROW_RANGE)
        ccol = Ranges(START_COLUMN_RANGE)
        column = self.encoded[:7]
        row = self.encoded[7:10]

        for r in row:
            if col == "F":
                crow = crow.f()
            elif col == "B":
                crow = crow.b()

        self.row = crow._range[0]

        for col in column:
            if col == "F":
                ccol = ccol.f()
            elif col == "B":
                ccol = ccol.b()

        self.column = ccol._range[0]

    @property
    def seat_id(self):
        return self.row * 8 + self.column




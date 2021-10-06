
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
    def __init__(self, ranges):
        self._range = ranges

    def first(self):
        return Ranges(self._range[:len(self._range)//2])

    def last(self):
        return Ranges(self._range[len(self._range)//2:])


class Seat:
    def __init__(self, encoded):
        self.encoded = encoded
        self.column = 0
        self.row = 0
        self.parse()

    def parse(self):
        utils.debug(f'Parsing {self.encoded}')
        crow = Ranges(START_ROW_RANGE)
        ccol = Ranges(START_COLUMN_RANGE)
        row = self.encoded[:7]
        column = self.encoded[7:10]
        utils.debug(f'Column: {column}')
        utils.debug(f'   Row: {row}')

        for r in row:
            utils.debug(f'iterate {row}: current {r}')
            if r == "F":
                crow = crow.first()
            elif r == "B":
                crow = crow.last()
            else:
                utils.error('Invalid row identifier')

        self.row = crow._range[0]

        for col in column:
            utils.debug(f'iterate {column}: current {col}')
            if col == "R":
                ccol = ccol.last()
            elif col == "L":
                ccol = ccol.first()
            else:
                utils.error('Invalid column identifier')

        self.column = ccol._range[0]

    @property
    def seat_id(self):
        return self.row * 8 + self.column


ids = []

for i in puzzle.splitlines():
    s = Seat(i)
    utils.debug(f'Col: {s.column}'.ljust(10) + f'Row: {s.row}'.ljust(10) + f'ID: {s.seat_id}')
    ids.append(s.seat_id)

utils.info('sorting ids')
ids.sort()

utils.info(f'Highest ID: {ids[-1]}')


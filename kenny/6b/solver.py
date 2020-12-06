
import sys

sys.path.extend(['../'])
import utils

utils.info('Solver for day 6a')

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


class Person:
    __slots__ = ('answers', )
    def __init__(self, ans):
        self.answers = []
        for i in ans:
            self.answers.append(i) if i not in self.answers else 0
        #print(self.answers)

    def __len__(self):
        return len(self.answers)


class Group:
    def __init__(self, answers):
        self.answers = answers
        self.people = []
        self.parse()
    
    def parse(self):
        raw_ans = self.answers.strip()

        for c, i in enumerate(raw_ans.splitlines()):
            person = Person(i)
            if c == 0:
                self.answers = person.answers
                continue
            for bor in self.answers:
                if bor not in person.answers:
                    self.answers.remove(bor)

    def __len__(self):
        return len(self.answers)

count = 0
for i in puzzle.strip().split('\n\n'):
    gp = Group(i)
    utils.debug(f'Group answers: {gp.answers} length {len(gp)}')
    count += len(gp)


utils.info(f'total answers: {count}')


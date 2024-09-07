import collections
from pprint import pprint
# from collection import deque
#
# # collections.deque
#
# # deq = deque()
#
# chain_map = collections.ChainMap()
#
# baseline = {'music': 'bach', 'art': 'rembrandt'}
# adjustments = {'art': 'van gogh', 'opera': 'carmen'}
# chain_map(adjustments, baseline)

# from collections import ChainMap
from collections import ChainMap
import pprint

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
pprint.pprint(ChainMap(adjustments, baseline))
pprint.pprint(list(ChainMap(adjustments, baseline)))

combined = baseline.copy()
combined.update(adjustments)
pprint.pprint(combined)


# deque = collections.deque()

import os, argparse

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

pprint.pprint(namespace)
pprint.pprint(command_line_args)

combined = ChainMap(command_line_args, os.environ, defaults)
pprint.pprint(combined)


# Tally occurrences of words in a list
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
pprint.pprint(cnt)

# Tally occurrences of words in a list
cnt = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
pprint.pprint(cnt)

from collections import Counter

c = Counter()                           # a new, empty counter
print(c)

c = Counter('gallahad')                 # a new counter from an iterable
print(c)

c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print(c)

c = Counter(cats=4, dogs=8)             # a new counter from keyword args
print(c)


import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

result = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

print(result)

from collections import namedtuple
from operator import attrgetter
from bisect import bisect, insort
from pprint import pprint

Movie = namedtuple('Movie', ('name', 'released', 'director'))

movies = [
    Movie('Jaws', 1975, 'Spielberg'),
    Movie('Titanic', 1997, 'Cameron'),
    Movie('The Birds', 1963, 'Hitchcock'),
    Movie('Aliens', 1986, 'Cameron')
]

pprint(movies)

by_year = attrgetter('released')
movies.sort(key=by_year)

# by_year = attrgetter('released')
movies.sort(key=attrgetter('released'))


result = movies[bisect(movies, 1960, key=by_year)]
print(result)
print(bisect(movies, 1960, key=by_year))

romance = Movie('Love Story', 1970, 'Hiller')
insort(movies, romance, key=by_year)
pprint(movies)
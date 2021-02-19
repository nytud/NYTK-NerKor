"""
Provide basic stats about the corpus.
"""

import argparse
import os
import sys
from collections import defaultdict


MORPH_MARK = 'morph'
NO_MORPH_MARK = 'no-morph'
TOTAL = 'total'

SENT_KEY = 'sent'
TOKEN_KEY = 'token'


def incr(dic, prefix, key):
    dic[f'{prefix}-{key}'] += 1
    dic[f'{TOTAL}-{key}'] += 1


def main():
    """Do the thing."""
    args = get_args()

    stats = defaultdict(int) # TODO count B-I sequences intead of single tags!
    # traverse directories recursively
    for root, _, files in os.walk(os.path.curdir):
        for fname in filter(lambda x: 'conllup' in x, files):
            path = os.path.join(root, fname)

            morph_analysed = f'{NO_MORPH_MARK}'
            if f'{os.sep}{MORPH_MARK}{os.sep}' in path:
                morph_analysed = f'{MORPH_MARK}'

            # because sent separators are counted
            incr(stats, morph_analysed, SENT_KEY)
            with open(path, encoding='utf-8') as infile:
                for line in infile:
                    line = line.strip()
                    if len(line) == 0:
                        incr(stats, morph_analysed, SENT_KEY)
                    elif '\t' in line:
                        incr(stats, morph_analysed, TOKEN_KEY)
                        fields = line.split('\t')
                        tag = fields[5]
                        incr(stats, morph_analysed, tag)

    for k, v in sorted(stats.items()):
        print(f'#{k}\t{v}')


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # string-valued argument
    parser.add_argument(
        '-s', '--smiley',
        help='add smiley',
        type=str,
        default=':)'
    )
    # boolean argument: True if present, False if not present
    parser.add_argument(
        '-d', '--duplicate',
        help='do something twice',
        action='store_true'
    )
    
    return parser.parse_args()


if __name__ == '__main__':
    main()

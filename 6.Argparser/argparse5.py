import argparse
parser=argparse.ArgumentParser()

parser.add_argument('--three',nargs=3)
parser.add_argument('--optional',nargs='?')
parser.add_argument('--all',nargs='*',dest='all')
parser.add_argument('--one-or-more',nargs='+')

print(parser.parse_args())

# output
# python argparse5.py --three 9 8 7
#Namespace(three=['9', '8', '7'], optional=None, all=None, one_or_more=None)
# python argparse5.py --optional 9
#Namespace(three=None, optional='9', all=None, one_or_more=None)

import sys
import argparse
parser = argparse.ArgumentParser(
    description = 'Калькулятор'
)
parser.add_argument(
    'values',
    metavar = 'VALUES',
    type = float,
    nargs = '+',
    help = 'входные данные'
)
parser.add_argument(
    '-a',
    '--action',
    type = str,
    action = 'store'
)

parser.add_argument(
    '-v',
    '--verbose',
    action = 'store_true',
)
args = parser.parse_args()
x = 0
y = 0
z = 0
if args.action=='+':
    x = args.values[0]
    y = args.values[1]
    z = x + y

if args.action=='-':
    x = args.values[0]
    y = args.values[1]
    z = x - y

if args.action=='*':
    x = args.values[0]
    y = args.values[1]
    z = x * y
if args.action=='/':
    x = args.values[0]
    y = args.values[1]
    z = x / y

if args.verbose:
    print(x,args.action,y,'=',z)
else:
    print(z)






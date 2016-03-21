from sys import argv
import argparse
import os
parser = argparse.ArgumentParser(
    description = 'Tree'
)
parser.add_argument(
    'filename',
    metavar = 'FILENAME',
    type = str,
    nargs = '+',
    help = 'Директории'
)
parser.add_argument(
    '--folders_only',
    action = 'store_true'
)

parser.add_argument(
    '--include',
    type = str,
    action = 'store',
)

parser.add_argument(
    '--exclude',
    type = str,
    action = 'store',
)
args = parser.parse_args()
files = args.filename

if args.include:
    files = [some_text for some_text in files if args.include in some_text]
if args.exclude:
    files = [some_text for some_text in files if args.exclude not in some_text]
for i in files:
    if not os.path.isdir(i):
        print('Указанный путь не существует или не является папкой')
        exit()

def tree(i):
    derevo = []
    content = os.listdir(i)
    if args.include:
        content = [file for file in content if args.include in file]
    if args.exclude:
        content = [file for file in content if not (args.include in file)]
    for file in content:
        if os.path.isdir(i + "/" + file):
            derevo.append(file + '\n' + '\n'.join(['->' + i for i in tree(i + '/' + file).split('\n')]))
        elif not args.folders_only:
            derevo.append(file)
    return '\n'.join(derevo)


for i in files:
    print('\n', 'Путь к данной директории:', '\n',os.path.abspath(i))
    print('\n','Содержимое:', '\n',tree(i))

import sys
import argparse
parser = argparse.ArgumentParser(
    description = 'Чтение файла'
)

parser.add_argument(
    'filename',
    metavar = 'FILE_NAME',
    type = str,
    nargs = '+',
    help = 'входные данные'
)

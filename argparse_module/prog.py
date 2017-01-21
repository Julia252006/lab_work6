import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('-sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

print(parser.print_help())
print(args.accumulate(args.integers))

# cd presentation/argparse_module
# python prog.py 1 2 3 4
# python prog.py 1 2 3 4 -sum
# python prog.py a b c
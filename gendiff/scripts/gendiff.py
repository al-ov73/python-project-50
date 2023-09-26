import argparse
import json


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str, help='')
parser.add_argument('second_file', type=str, help='')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()

def generate_diff(first_file, second_file):
    print(args)
    f = json.load(open(first_file))
    print(f)

def main(first, second):
    generate_diff(first, second)
    
main(args.first_file, args.second_file)
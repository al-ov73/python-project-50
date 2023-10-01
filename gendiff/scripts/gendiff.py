import argparse
from gendiff import generate_diff
from gendiff import stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str, default='stylish', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'stylish':
        formated_result = stylish(diff)
    print(formated_result)


if __name__ == '__main__':
    main()

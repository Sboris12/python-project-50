import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()

    print(f"Diff between: {args.first_file} and {args.second_file}")
    print(f"Format: {args.format}")

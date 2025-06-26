from hexlet_code.cli import parse_args
from hexlet_code.gendiff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

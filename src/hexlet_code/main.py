from hexlet_code.json_handler import load_json


def main():
    filenames = ['file1.json', 'file2.json']
    for name in filenames:
        data = load_json(name)
        print(f"\n{name} content:")
        print(data)


if __name__ == '__main__':
    main()

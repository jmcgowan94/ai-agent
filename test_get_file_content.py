from functions.get_file_content import get_file_content

def test():
    tests = [['calculator', 'main.py'], ['calculator', 'pkg/calculator.py'], ['calcualtor', '/bin/cat'], ['calculator', 'pkg/does_not_exist.py']]

    for test in tests:
        print(get_file_content(test[0], test[1]))


if __name__ == "__main__":
    test()

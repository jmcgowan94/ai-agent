from functions.get_files_info import get_files_info

def test():
    tests = [['calculator', '.'], ['calculator', 'pkg'], ['calcualtor', '/bin'], ['calculator', '../']]

    for test in tests:
        print(f'Result for {'current' if test[1] == '.' else test[1]} directory:')
        print(get_files_info(test[0], test[1]))


if __name__ == "__main__":
    test()

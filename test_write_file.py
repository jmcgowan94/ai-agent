from functions.write_file import write_file

def test():
    tests = [["calculator", "lorem.txt", "wait, this isn't lorem ipsum"], ["calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"], 
             ["calcualtor", "/tmp/temp.txt", "this should not be allowed"]]

    for test in tests:
        print(write_file(test[0], test[1], test[2]))


if __name__ == "__main__":
    test()

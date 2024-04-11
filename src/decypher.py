import sys


def core() -> None:
    argc = len(sys.argv)
    if argc != 1:
        for index in range(1, len(sys.argv)):
            if len(sys.argv[index]) != 0:
                print(''.join(i[0] for i in sys.argv[index].rstrip().split()))
    else:
        print("[ERROR] You forgot to give a line for study")


if __name__ == '__main__':
    core()

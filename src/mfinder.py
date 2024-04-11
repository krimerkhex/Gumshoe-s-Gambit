import sys
import re


def core() -> None:
    stdin = sys.stdin.read()
    if len(stdin) != 0:
        pattern = stdin.rstrip().split()
        reg = [re.compile('[*][^*]{3}[*]'), re.compile('[*]{2}[^*][*]{2}'), re.compile('[*][^*][*][^*][*]')]
        if len(pattern) == 3 and len(pattern[0]) == 5 and len(pattern[1]) == 5 and len(pattern[2]) == 5:
            print(True if reg[0].search(pattern[0]) and reg[1].search(pattern[1]) and reg[2].search(
                pattern[2]) else False)
        else:
            print("ERROR")
    else:
        print("[ERROR] STDIN is empty")


if __name__ == '__main__':
    core()

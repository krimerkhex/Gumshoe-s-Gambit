import re
import sys


def core(count_need_reed, stdin) -> None:
    counter = 0
    for line in stdin:
        line = line.rstrip()
        if counter < count_need_reed or count_need_reed == -1:
            if len(line) == 32 and line[:5] == "00000" and line[5] != '0':
                print(line)
        counter += 1


def main() -> None:
    if len(sys.argv) == 1:
        core(-1, sys.stdin)
    elif len(sys.argv) == 2 and re.fullmatch("\d*", sys.argv[1]) and 0 < int(sys.argv[1]):
        core(int(sys.argv[1]), sys.stdin)
    else:
        print(f"[Error] {sys.argv[1]} is uncorrect gived to read")


if __name__ == '__main__':
    main()

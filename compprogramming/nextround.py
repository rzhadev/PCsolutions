#!/usr/bin/env pypy
import sys


def main():
    info = sys.stdin.readline().split()
    n = int(info[0])
    k = int(info[1])-1
    part = sys.stdin.readline().split()
    min_score = int(part[k])
    count = 0
    for score in part:
        if int(score) >= min_score and int(score) > 0:
            count += 1

    sys.stdout.write(str(count))


if __name__ == "__main__":
    main()

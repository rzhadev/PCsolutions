#!/usr/bin/env pypy
import sys


def main():
    length = sys.stdin.readline()
    inputs = [(lambda a: [int(i) for i in a])(string.split())
              for string in sys.stdin.readlines()]
    sum_vec = [0, 0, 0]
    for vector in inputs:
        sum_vec[0] += vector[0]
        sum_vec[1] += vector[1]
        sum_vec[2] += vector[2]
    out = "YES" if sum_vec[0] == 0 and sum_vec[1] == 0 and sum_vec[2] == 0 else "NO"   # noqa
    print(out)


if __name__ == "__main__":
    main()

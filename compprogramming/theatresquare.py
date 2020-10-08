#!/usr/bin/env pypy
import sys


def main():
    info = sys.stdin.readline().split()
    dim1 = int(info[0])
    dim2 = int(info[1])
    a = int(info[2])
    flagstones = (dim1 + (a-1)) // a
    flagstones *= (dim2 + (a-1)) // a
    print(flagstones)


if __name__ == "__main__":
    main()

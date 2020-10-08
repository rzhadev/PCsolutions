#!/usr/bin/env pypy
import sys


def main():
    words = sys.stdin.readlines()
    length = words.pop(0)
    for word in words:
        if (len(word)-1) > 10:
            # don't include \n character and first and last characters
            skip = len(word)-2-1
            new = word[0]+str(skip)+word[-2]+'\n'
            sys.stdout.write(new)
        else:
            sys.stdout.write(word)


if __name__ == "__main__":
    main()

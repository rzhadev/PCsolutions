#!/usr/bin/env pypy
import sys


def main():
    vowels = "aeiouyAEIOUY"
    string = sys.stdin.readline()
    new_str = ""
    for char in string:
        if char not in vowels and char != "\n":
            new_str += "."
            if char == char.upper():
                new_str += char.lower()
            else:
                new_str += char

    print(new_str)


if __name__ == "__main__":
    main()

#!/usr/bin/env pypy
import sys
import re


def main():
    word = input()
    x = 0
    for i in range(len(word)):
        if word[i] == 'h' and x == 0:
            x += 1
        elif word[i] == 'e' and x == 1:
            x += 1
        elif word[i] == 'l' and x == 2:
            x += 1
        elif word[i] == 'l' and x == 3:
            x += 1
        elif word[i] == 'o' and x == 4:
            x += 1
    print("YES") if x == 5 else print("NO")


if __name__ == "__main__":
    main()

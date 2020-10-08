#!/usr/bin/env pypy
import sys

# if a string is odd, then all characters must be equal
# to be good.
# if a string is even, then all characters of s_i and s_1+2 must be equal
# in other words, every other character must be equal to one another


def main():
    for _ in range(int(input())):
        s = input()
        max_ = 0
        for i in range(10):
            for j in range(10):
                max_ = max(max_, solve(s, str(i), str(j)))

        print(len(s)-max_)

# s1 is the original string


def solve(s1, x, y):
    # try to create the longer string of consecutive x,y
    # if the value of greed (or the length of the construction)
    # is odd, then x and y will be equal
    greed = 0
    for char in s1:
        if char == x:
            greed += 1
            z = x
            x = y
            y = z
    # if the string has a length that is odd,
    # and the first 2 characters are not equal
    # then you would have to remove a character
    if (greed % 2 == 1 and x != y):
        greed -= 1

    return greed


if __name__ == "__main__":
    main()

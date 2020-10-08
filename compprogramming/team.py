#!/usr/bin/env pypy
import sys


def main():
    length = sys.stdin.readline()
    probs = sys.stdin.readlines()
    prob_count = 0
    for prob in probs:
        prob = prob.replace(" ", "")
        prob = prob.replace("\n", "")
        count = int(prob[0]) + int(prob[1]) + int(prob[2])
        if count >= 2:
            prob_count += 1

    sys.stdout.write(str(prob_count))


if __name__ == "__main__":
    main()

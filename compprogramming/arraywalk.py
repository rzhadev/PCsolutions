#!/usr/bin/env pypy
import sys

# -cant do >= 2 moves to the left in a row
# -cant exceed z moves to the left total
# -k moves in total


def main():
    length = int(sys.stdin.readline())
    # -there are k moves total, with k-t moves to the left
    # -ending position in the array is
    # determined by how many moves to the left are used
    # -because only one move to the left can be used at a time,
    # we know that the ending position is k-2*t,
    # where t is the number of moves to the left
    # thus, for each case of position (1,k-2*t),
    # calculate the maximum (i, i+1) pairing
    # that would be used for a left move
    # then find the sum by adding the sum from the right moves
    # plug max_ (maximum move pair value) * t (number of left moves)
    for i in range(length):
        n, k, z = map(int, input().split())  # noqa
        a = (lambda x: [int(i) for i in x])(input().split())
        ans = 0
        for left in range(z+1):
            end_pos = k - 2 * left
            max_ = 0
            s = 0
            for i in range(end_pos+1):
                if i < n - 1:
                    # find the current best (left,right) pairing
                    max_ = max(max_, a[i]+a[i+1])
                s += a[i]
            ans = max(ans, s+max_ * left)
        print(ans)


if __name__ == "__main__":
    main()

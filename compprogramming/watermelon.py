import sys


def main():
    weight = int(sys.stdin.readline())
    if weight % 2 == 0 and weight > 2:
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == "__main__":
    main()

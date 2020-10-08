#!/usr/bin/env pypy
import sys

# clean = lexicographically the smallest, and the shortest
# OR no possible moves can be made
# thus, if the string cant be cleaned when theres no possible actions left
# for every pairing of s_i = "1" and s_i+1 = "0", there are 2n actions possible
def main():
    n = int(input())
    for _ in range(n):
        length = int(input())
        string = input()
        if(dec(string) or len(string) == 1):
            print(string)
        else:
            x = 1
            y = 0
            for i in range(len(string)):
                if(string[i] == "0"):
                    x += 1
                else: 
                    break
            for j in range(len(string)):
                if(string[len(string)-1-j] == "1"):
                    y += 1
                else:
                    break
            s = ""
            for _ in range(x):
                s += "0"
            for _ in range(y):
                s += "1"
            print(s)
           
def dec(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True
if __name__ == "__main__":
    main()

def main():
    length = int(input())
    for z in range(1, length+1):
        arr = [int(i) for i in input().split(' ')]
        n = arr[0]
        a = arr[1] # left->right
        b = arr[2] # right->left
        c = arr[3] # seen by both
        if (a + b - c) > n or ((a + b - c) == 1 and n >= 2):
            print("Case #%s: IMPOSSIBLE" % z)
        elif n == 1:
            print("Case #%s: 1" % z)
        elif n == 2:
            if c == 2:
                print("Case #%s: 1 1" % z)
            elif a == 2:
                print("Case #%s: 1 2" % z)
            elif b == 2:
                print("Case #%s: 2 1" % z)
        else:
            comp = []
            for i in range(a-c):
                comp.append(2)
            for j in range(c):
                comp.append(3)
            for l in range(b-c):
                comp.append(2)
            extra = n - (a + b - c)
            if extra > 0:
                for i in range(extra):
                    comp.insert(1, 1)
            s = ""
            for xi in range(len(comp)):
                if xi < (len(comp)-1):
                    s += str(comp[xi]) + " "
                else:
                    s += str(comp[xi])
            print("Case #%s: %s" % (z, s))
            



if __name__ == "__main__":
    main()
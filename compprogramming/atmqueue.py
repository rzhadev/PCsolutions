import math
def main():
    length = int(input())
    for b in range(length):
        inp = [int(i) for i in input().split(' ')]
        N = inp[0]
        X = inp[1]
        queue = [int(i) for i in input().split(' ')]
        K = [(math.ceil(queue[i]/X), i+1) for i in range(len(queue))]
        K = sorted(K)
        s = ""
        for x,y in K:
            s += " "+str(y)
        s = s[1:]
        print("Case #%s: %s" % (b+1,s))    
        

if __name__ == "__main__":
    main()
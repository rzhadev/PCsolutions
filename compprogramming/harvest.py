'''
3 5
1 5
10 11
8 9

3 2
1 2
3 5
13 14
'''
# find how many intervals overlap with K
def main():
    n = int(input()) 
    for x in range(1, n+1):
        s = [int(i) for i in input().split(' ')]
        N = s[0]
        K = s[1]
        times = []
        count = 1
        for _ in range(N):
            times.append([int(i) for i in input().split(' ')])
        
        for x in times:
            pass

        #print("Case #%s: %s" % (x,maxl))
        
if __name__ == "__main__":
    main()
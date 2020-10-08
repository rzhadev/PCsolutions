def main():
    n = int(input()) 
    for x in range(1, n+1):
        length = int(input())
        arr = [int(i) for i in input().split(' ')]
        difs = []
        for i in range(0, len(arr)-1):
            difs.append(arr[i+1]-arr[i])
        
        maxl = 0
        count = 1
        currdif = difs[0]
        for dif in difs:
            if currdif == dif:
                count += 1
            else:
                count = 2
                currdif = dif
            maxl = max(maxl, count)
        
        print("Case #%s: %s" % (x,maxl))
        
if __name__ == "__main__":
    main()
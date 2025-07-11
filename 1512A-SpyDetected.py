t = int(input())

for i in range(t):
    n = int(input())
    
    lt = list(map(int, input().split()))

    def fun():
        spy_ind = -1
        good = 0

        for i in range(n):
            if lt[i] == lt[good]:
                continue
                
            if spy_ind != -1 and lt[i] == lt[spy_ind]:
                return good
            spy_ind = i
        
        return spy_ind

    print(fun() + 1)
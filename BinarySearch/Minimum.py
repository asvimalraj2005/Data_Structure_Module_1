# Provided an array, find any one local minima 
# Below is the code for the above problem
def solve():
    t=int(input())
    for _ in range(t):
        a=list(map(int,input().split()))
        l=0
        N=len(a)
        r=N-1
        while(l<=r):
            mid=(l+r)//2
            if ((mid==0 or a[mid-1]>=a[mid])) and (mid==N-1 or a[mid+1]>=A[mid]):
                print(mid)
            elif (mid==0 or a[mid-1] >= a[mid]):
                l=mid+1
            else:
                r=mid-1
            
solve()

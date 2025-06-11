# Provided a number n find the squareroot of n
# Below is the code for the above problem statement 
def squareroor(N):
    ans=0
    l=1
    r=N
    while(l<=r):
        m=l+(r-l)//2
        if m*m==N:
            print(m)
            return
        elif m*m>N:
            r=m-1
        elif m*m<N:
            ans=m
            l=m+1
    print(ans)

squareroor(25)
            
    
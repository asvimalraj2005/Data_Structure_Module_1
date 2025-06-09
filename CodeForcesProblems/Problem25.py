# https://codeforces.com/problemset/problem/155/A
# Below is the code for the above problem link 
def Problem25():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        count=0
        for i in range(1,len(a)):
            if a[i]>a[i-1]:
                count=count+1
    print(count)

Problem25()
            
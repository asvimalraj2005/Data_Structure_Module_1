# Good Arrays 
# https://codeforces.com/problemset/problem/1856/B
# Below is the code 
def Problem21():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if len(set(a))==1:
            print("NO")
        else:
            print("YES")

Problem21()
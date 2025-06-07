# Good Arrays 
# https://codeforces.com/problemset/problem/1856/B
# Below is the code 
def Problem21():
    t=int(input())
    for _ in range(t):
        a=list(map(int,input().split()))
        n=len(a)
        list_set=set(a)
        n1=len(list_set)
        if n1==1:
            print("No")
        else:
            print("Yes")

Problem21()
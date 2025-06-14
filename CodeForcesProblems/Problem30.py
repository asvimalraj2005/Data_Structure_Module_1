# https://codeforces.com/problemset/problem/1095/B
# Below is the code for the above problem 
def solve():
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().split()))
    a.sort()
    instability1 = a[-1] - a[1]  
    instability2 = a[-2] - a[0]  
    print(min(instability1, instability2))

solve()

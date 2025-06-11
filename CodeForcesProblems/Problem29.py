# https://codeforces.com/problemset/problem/1418/A 
def solve():
    t = int(input())
    for _ in range(t):
        m, n, v = map(int, input().split())
        total_sticks_needed = v * (n + 1)
        stick_= (total_sticks_needed - 1 + (m - 2)) // (m - 1)
        print(stick_ + m)
solve()

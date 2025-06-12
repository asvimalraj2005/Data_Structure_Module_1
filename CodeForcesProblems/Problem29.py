<<<<<<< HEAD
# https://codeforces.com/problemset/problem/1418/A 
def solve():
    t = int(input())
    for _ in range(t):
        m, n, v = map(int, input().split())
        total_sticks_needed = v * (n + 1)
        stick_= (total_sticks_needed - 1 + (m - 2)) // (m - 1)
        print(stick_ + m)
solve()
=======
# https://codeforces.com/problemset/problem/1418/A 
def solve():
    t = int(input())
    for _ in range(t):
        x, y, k = map(int, input().split())
        total_sticks_needed = k * (y + 1)
        stick_trades = (total_sticks_needed - 1 + (x - 2)) // (x - 1)
        print(stick_trades + k)
solve()
>>>>>>> 3277c29 (Problem3)

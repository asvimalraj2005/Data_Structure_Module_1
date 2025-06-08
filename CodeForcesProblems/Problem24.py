# Max A and Max B multiplication
# https://codeforces.com/problemset/problem/1631/A
# Below is the code 
def Problem24():
    t=int(input())
    for _ in range(t):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a_max_element=max(a)
        b_max_element=max(b)
        print(a_max_element*b_max_element)
    
Problem24()
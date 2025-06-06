# Median Number 
# https://codeforces.com/problemset/problem/1760/A
# Medium Number 
# a,b,c sort them and return the first index element(0 position indexing)
# Below is the code 
def Problem14():
    t=int(input())
    for _ in range(t):
        a=sorted(list(map(int,input().split())))
        print(a[1])

Problem14()
        
        

    
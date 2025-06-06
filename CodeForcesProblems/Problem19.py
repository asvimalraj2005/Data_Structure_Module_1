# Prepend and Append 
# https://codeforces.com/problemset/problem/1791/C
# Straight forward approach 
# Below is the code 
def Problem19():
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=input()
        list_s=list(s)
        list_s.pop(0)
        list_s.append('1')
        list_s=''.join(list_s)
        decimal_number=int(list_s,2)
        print(decimal_number)
        

Problem19()
        
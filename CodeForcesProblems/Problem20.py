# AB Balance
# https://codeforces.com/problemset/problem/1606/A
# Input : 4 
#         b             -> b             <>      0 
#         aabbbabaa     -> aabbbabaa     <>      ab ab 2  ;   ba ba 2   
#         abbb          -> bbbb          <>      ab    1  ;   ba    0
#         abbaab        -> abbaaa        <>      ab ab 2  ;   ba    1         
# Below is the code 
def Problem20():
    t=int(input())
    for _ in range(t):
        s=input()
        count_of_a=0
        count_of_b=0
        s_list=list(s)
        for i in range(len(s_list)-1):
            if s_list[i]=='a' and s_list[i+1]=='b':
                count_of_a=count_of_a+1
        for j in range(len(s_list)-1):
            if s_list[i]=='b' and s_list[i+1]=='a':
                count_of_b=count_of_b+1 
        
        print(count_of_a)
        print(count_of_b)
        
        
Problem20()
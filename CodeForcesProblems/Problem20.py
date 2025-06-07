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
        count_of_ab=0
        count_of_ba=0
        s_list=list(s)
        if len(s)==1:                                       # For input like a or b 
            print(s)
            continue
        for i in range(len(s_list)-1):
            if s_list[i]=='a' and s_list[i+1]=='b':
                count_of_ab=count_of_ab+1
        for j in range(len(s_list)-1):
            if s_list[j]=='b' and s_list[j+1]=='a':
                count_of_ba=count_of_ba+1 
        if count_of_ab>count_of_ba:
            Found=False
            for m in range(len(s_list)):
                if s_list[m]=='b':
                    s_list[m]='a'
                    Found=True
                    break
        if count_of_ba>count_of_ab:
            Found=False
            for n in range(len(s_list)):
                if s_list[n]=='a':
                    s_list[n]='b'
                    Found=True
                    break 
        print(''.join(s_list))  
             
            
Problem20()                                         # This is the login I built on my own 

# This is the logic below from online reference


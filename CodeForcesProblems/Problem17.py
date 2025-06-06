# Blank Space 
# https://codeforces.com/problemset/problem/1829/B 
# Input : -> t test cases 
#            n is length of the array 
#            input containing n space separated integers 
# Just return the count of blank space i.e zeros inbetween ones (longest space)
# Below is the code 
def Problem17():
    t=int(input())
    for _ in range(t):
        n=int(input())
        binary_array=list(map(int,input().split()))                     # Input array named binary_array 
        space=0                                                         # Space to count the spaces i.e zeros between two ones, first on the left side ; second on the right side inbetween them zeros are filled 
        max_space=0                                                     # For every 1-1 , zeros are filled in lower order or higher order to follow them up an max_space is used to find the maximum of the zeros 
        for i in range(n):                                              # Login 
            if binary_array[i]==0:
                space=space+1 
                max_space=max(space,max_space)
            if binary_array[i]==1:
                space=0
        print(max_space)
    
Problem17()
    
        

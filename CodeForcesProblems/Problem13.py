# Little XOR 
# https://codeforces.com/problemset/problem/252/A
# Someone likes arrays that consist of non-negative integers a lot. 
# Recently his friend has presented him one such array consisting of n elements. Immediately decided to find 
# there a segment of consecutive elements, such that the xor of all numbers from this segment was maximal possible 
# Input : The first line contains integers n (1<=n<=100) the number of elements in the array. The second line 
# contains the space-separated integers from the array. All numbers are non-negative integers strictly less than 2^30
# Output : Print a single integer the required maximal xor of a segment of consecutive elements 
# 5                                                  3 
# 1 2 1 1 2                   8 4 2 1                1 2 7          8 4 2 1 
# 3                     1     0 0 0 1                7        1     0 0 0 1
#                       2     0 0 1 0                         2     0 0 1 0
#                       1     0 0 0 1                         7     0 1 1 1
#                       1     0 0 0 1                                 1 1 1  -> 7   
#                       1     0 0 0 1 
#                       2     0 0 1 0 
#                                 1 1  -> 3      
# Below is the problem solving approach 
# 5 is the length and using the length we are creating a for loop of range 5 and by using the input function, the number have been appended to the list 
def Problem():
    n=int(input())
    list_num=[]
    for i in range(n):
        list_num.append(int(input()))
                                                    # Now we got the numbers from the user that are kept in the list_num 
    # Coverting the decimal number to binary format and storing into new list 
    bin_list=[]
    for e in list_num:
        bin=format(e,'b')
        bin_list.append(bin)
    
    bin_list_2=' '.join(bin_list)
    

Problem()
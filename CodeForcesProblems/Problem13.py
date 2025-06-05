# Little XOR 
# https://codeforces.com/problemset/problem/252/A
# Someone likes arrays that consist of non-negative integers a lot. 
# Recently his friend has presented him one such array consisting of n elements. Immediately decided to find 
# there a segment of consecutive elements, such that the xor of all numbers from this segment was maximal possible 
# Input : The first line contains integers n (1<=n<=100) the number of elements in the array. The second line 
# contains the space-separated integers from the array. All numbers are non-negative integers strictly less than 2^30
# Output : Print a single integer the required maximal xor of a segment of consecutive elements 
# 5                    
# 1 2 1 1 2
# 3 
# Below is the problem solving approach 
# 5 is the length and using the length we are creating a for loop of range 5 and by using the input function, the number have been appended to the list 
def Problem():
    n = int(input())                            # length
    a = list(map(int, input().split()))         # input integers 
    max_xor = 0                                 # variable used for storing the max xor sum 
    for i in range(n):                          # loop used to run until reaching the length of the array 
        xor_sum = 0                             # xor_sum initialised as zero
        for j in range(i, n):                   # consecutive arrays 
            xor_sum ^= a[j]                     # XOR-ing the numbers 
            max_xor = max(max_xor, xor_sum)     # Max of all the XOR in the consecutive arrays 

    print(max_xor)                              # Returning the answer 

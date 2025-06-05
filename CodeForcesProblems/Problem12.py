# Day at the beach 
# https://codeforces.com/problemset/problem/599/C
# One day squidward, Spongebob and Patrick decided to go to the beach. Unfortunately, the weather was bad, so the friends were unable to ride waves. However, 
# they decided to spent their time building sand castles. At the end of the day there were n castles built by friends. Castles are numbered from 1 to n, and 
# the height of the i-th castle is equal to hi. when friends were about to leave, Squidward noticed, that castles are not ordered by their height, and this looks
# ugly. Now friends are going to reorder the castles in a way to obtains that condition hi<=hi+1 holds for all i from 1 to n-1. Squidward suggested the following
# process of sorting castles: Castles are split into blocks - groups of consecutive castles. Therefore the block from i to j will include castles i,i+1,...j.
# A block may consist of a single castle. The partitioning is chosen in such a way that every castle is a part of exactly one block. Each block is sorted independently
# from other blocks, that is the sequence hi,hi+1,.....,hj becomes sorted. The partitioning should satisfy the condition that after each block is sorted, the sequence 
# hi becomes sorted too. This may always be achieved by saying that the whole sequence is a single block. Even patrick understands that increasing the number of blocks 
# in partitioning will ease the sorting process. Now friends ask you to count the maximum possible number of blocks in a partitioning that satisfies all the above 
# requirements.
# Input : The first line of the input contains a single integer n (1<=n<=100000) the number of castles spongebob patrick and squidward made from sand during the day 
#         The next line contains n integers hi(1<=hi<=10^9). The i-th of these integers corresponds to the height of the i-th castle 
# Output : Print the maximum possible number of blocks in a valid partioning. 
# Input : 3 
#         1 2 3     -> 3
#         4 
#         2 1 3 2   -> 2 
# From the above problem statement : At the end of the day there were n castles built on that day 
#                                    castles are numbered from 1 to n
#                                    height of the ith castle is equal to hi
#                                    that castles are not ordered by their height
#                                    reordering them to obtain the condition hi<=hi+1 holds for all i from 1 to n-1 
#                                    The next line contains n integers hi (1 ≤ hi ≤ 109). The i-th of these integers corresponds to the height of the i-th castle.
#                                    just use sort method to sort the i-th integer values for the partitioning process 
#                              (skip)Remember same number should not be existed in other partitions i.e 2 1 3 2 after partition it becomes 1 2 2 3 where the split will be [1,2] [2,3] now there is two parition 
#                              (skip)On here 1 2 3 it's already in sorted position, where the maximum possible number of blocks in a valid patitioning is 3  
# Below is the code for the above problem statement
def day_at_the_beach():
    n = int(input())                 # Number of castles
    a = list(map(int, input().split()))  # Heights of castles

    b = sorted(a)                    # Sorted version for comparison
    freq_a = {}                      # Creating a dictionary for storing the key and value which relates to integer and occurrences 
    freq_b = {}
    blocks = 0
    for i in range(n):
        if a[i] in freq_a:
            freq_a[a[i]] += 1        # If present we are incrementing the count by one
        else:
            freq_a[a[i]] = 1         # If new just 1 
                                     # Count in sorted list
        if b[i] in freq_b:
            freq_b[b[i]] += 1
        else:
            freq_b[b[i]] = 1
                                    # If both frequency maps match, we can split here
        if freq_a == freq_b:
            blocks += 1

    print(blocks)                   # Printing the maximum no of blocks 
    #
    #
    # Solving bigger problems need a lot of time and patience, and online referrences for the learning and implementation process 


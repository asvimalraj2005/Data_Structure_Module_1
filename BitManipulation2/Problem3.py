# Problem Statement 
# Given binary List. Find the number of sub list having OR 1 
# For all i , A [i] = { 0 , 1 }
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1 
#
# Total No of Sub-List = N * ( N + 1 ) / 2   -->  Ans = 11
# A = [ 1 , 0 , 0 , 1 , 0 ]
#      ___                               OR 1  --> Yes
#      _______                           OR 1  --> Yes
#      ___________                       OR 1  --> Yes
#      _______________                   OR 1  --> Yes 
#      ___________________               OR 1  --> Yes
#          ___                           OR 1  --> No
#          _______                       OR 1  --> No
#          ___________                   OR 1  --> Yes
#          _______________               OR 1  --> Yes
#             ___                        OR 1  --> No
#             ________                   OR 1  --> Yes
#             ____________               OR 1  --> Yes
#                ___                     OR 1  --> Yes
#                _________               OR 1  --> Yes
#                     ____               OR 1  --> No                  YES --> Count => 11
#
# Total No of Sub List = No of sub List with OR 1 + No of sub List with OR 0
#                                                     All elements in sub List are 0 
# Below is the python code for the above problem statement 
#
def FindSubListwithOnesInThem(A):
    Count_Variable_0 = 0                                                                                                    # Used for reference for counting purpose 
    Count_Variable_1 = 0                                                                                                    # Used for reference for counting purpose 
    N = len(A)                
    for i in range(len(A)):                                                                                                 # Executing the loop from 0 to total length -1                      
        if A[i] == 0:                                                                                                       # A[i]==0 --> Says that we are accessing every element in the list where A[i]==0 we are incrementing the Count_Variable_1 by 1
            Count_Variable_1 = Count_Variable_1 + 1    
        else:                                                                                                               # If not the if conditions fails there else condition will get executed                                    
            Count_Variable_0 = Count_Variable_0 + (Count_Variable_1 * (Count_Variable_1 + 1)) // 2                          # It A[i]==1 then N*(N+1)//2 will be applied here 
            Count_Variable_1 = 0                                                                                            # Re_Initialising the Count_Variable_1 with 0 again for calculation of sub list with zero
    Count_Variable_0 = Count_Variable_0 + (Count_Variable_1 * (Count_Variable_1 + 1)) // 2                                  
    Count_Variable_Ans = (N * (N + 1)) // 2 - Count_Variable_0                                                              # Subtracting total no of sub list which consist of whole zeroes inthem with the sub list of containing both the zeroes and ones  

    return Count_Variable_Ans


A=[1,0,0,1,0]
print(FindSubListwithOnesInThem(A))
    

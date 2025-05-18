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
    Count_Variable_0 = 0
    Count_Variable_1 = 0
    N = len(A)
    for i in range(len(A)):
        if A[i] == 0:
            Count_Variable_1 = Count_Variable_1 + 1
        else:
            Count_Variable_0 = Count_Variable_0 + (Count_Variable_1 * (Count_Variable_1 + 1)) // 2
            Count_Variable_1 = 0
    Count_Variable_0 = Count_Variable_0 + (Count_Variable_1 * (Count_Variable_1 + 1)) // 2
    Count_Variable_Ans = (N * (N + 1)) // 2 - Count_Variable_0
    return Count_Variable_Ans


A=[1,0,0,1,0]
print(FindSubListwithOnesInThem(A))
    

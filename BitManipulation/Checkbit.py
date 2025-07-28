# Problem Statement 
# Check whethee i th bit is set or not 
# Explanation : take an number 120 
#                                                      8   7    6    5    4    3   2   1   0 (index)
# Now using the 8 4 2 1 bit calculating method here ->256  128  64   32   16   8   4   2   1 
#                                                      0   0    1    1    1    1   0   0   0 
# Now checking the if the i th bit is set or not        ↑ the i th bit is not set 
#
# Below is the python code for the above approach
#
def CheckBit(A,i):
    if(A&(1<<i))==0: return False
    else : return True
    

A=120
i=8                                                     # 256 bit significance range
print(CheckBit(120,i))                                  # The answer will be False 


A=128
i=8
print(CheckBit(128,i))                                  # The answer will be True


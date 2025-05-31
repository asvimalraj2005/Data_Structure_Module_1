# Problem Description
# You are given a function isalpha() consisting of a character A 
# Return 1 if all the characters of a character array are alphanumeric [a-z,A-Z,and 0-9]
# Input Format : Only argument is a character array A 
# Output format : Return 1 if all the characters of the character array are alphanumeric[a-z,A-Z,0-9]
#                 else return 0 
# Input : A['s','c','a','l','e','r','#','2','0','2','0']
# Ouput : 0 
# Explanation : all the characters are not alphanumeric
#
# below is the coe for the above problem statement 
# 
def solve(A):
    for ch in A:                    # Traversing the string A through using the for loop with the iterator ch
        if not ch.isalnum():        # validating if the ch is not satisfying the isalphanumeric function() if it does not satisfies we are returning 0 
            return 0                
    return 1                        # If all the characters satisfies the isalnum() then we are returning 1 

A = ['s','c','a','l','e','r','2','0','2','0']   # Passing the literals of string values in a list 
print(solve(A))                                 # The result will be printed here 



            
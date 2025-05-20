# Problem Description 
# Write a recursive function that checks whether string A is a palindrome or Not.
# Return 1 if the string A is a palindrome, else return 0.
# Note : A palindrome is a string that's the same when read forward and backward 
# Input Format : The first and only argument is a string A.
# Output Format : Return 1 if the string A is a palindrome, else return 0.
# Input = "naman"
# Output = "1"
# Explanation 1: "naman" is a palindomic string, so return 1.
# Signature of the function should not get changed
# Approach just a use helper function where two pointers with pointer_1=0 and pointer_2 with the value of N-1 
# The helper function will recursively checks the first value and the last value if it same then pointer_1=pointer_1+1 and pointer_2=pointer_2-1 if pointer_1 is not equal to pointer_2 then we return 0 and if pointer_1 <= pointer_2 should have to get satisfied 
# Below is the python code 
def PalindromeString(A):
    def Helper(A,Start,End):
        if Start>=End:
            return 1
        if A[Start]!=A[End]:
            return 0
        return Helper(A,Start+1,End-1) 
    return Helper(A,0,len(A)-1)

print(PalindromeString("TurnAround"))

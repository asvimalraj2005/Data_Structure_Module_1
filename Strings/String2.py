# Problem Description
# Akash likes playing with strings. One day he thought of applying following operations 
# on the string in the given order 
# Concatenate the string with itself
# Delete all the uppercase letters 
# Replace each vowel with '#'
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return
# the resultant string after applying the above operations 
# Note : 'a','e','i','o','u'
# Input Format : First argument is a string A of size N
# Output Format : Return the resultant string 
# Example explanation : A = "aeiOUz"
#                     O/P = "###z###z"
#
# First concatenate the string with itself so string A becomes "aeiOUzaeiOUz"
# Delete all the uppercase letters so string becomes "aeizaeiz". Now replace vowel with '#', A becomes "###z###z"
#
#
def Solve(A):
    A=A+A                                # Concatenating string A with itself
    result=''                            # Creating an empty string named result 
    vowels={'a','e','i','o','u'}         # Storing the vowels in an set 
    for ch in A:                         # Iterating over the A 
        if ch.isupper():                 # If the iterating value over A is Upper character 
            continue                     # we are continuing 
        if ch in vowels:                 # If the value in the A is found to be having any vowel character then we are changing the character from a alphabet to "#"
            result += '#'
        else:                            # Else result=result+ch
            result += ch
    return result                        # Returning the result 
A = "aeiOUz"
print(Solve(A))  




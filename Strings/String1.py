# Problem Description
# You are given a character string A having length N, Consisting of only lowercase and uppercase latin letters 
# You have to toggle case of each character of string A. For example 'A' is changed to 'a', 'e' is changed to 'E' etc
# Input Format : First and only argument is a character string A 
# Output Format : Return a character string 
# Example explanation  Input  : "Hello"
#                      Output : "hELLO"
# 
# Below is the program code to change the lower case alphabets to upper case alphabets 
# and uppercase alphabets to lower case alphabets 
# 
def Solve(A):                           # The string is passed to the Solve function 
    result = ''                         # Creating an empty variable where there are no alphabets is stored 
    for ch in A:                        # Traversing A string variable 
        if ch.islower():                # If any alphabet is lower in the ch iterator 
            result+=ch.upper()          # We are appending the alphabet to the result by using upper() function 
<<<<<<< HEAD
            
=======
>>>>>>> 74973f2aa4ae02848f1c7dd559706885675d7bec
        elif ch.isupper():              # If any alphabet is upper in the ch iterator
            result+=ch.lower()          # we are appending the alphabet to the result by using lower() function 
        else:
            result+=ch                  # if it is a special case we are appending 
    return result                       # Returning the result 

A = "Data Structure"
print(Solve(A))  # Output: "dATA sTRUCTURE"

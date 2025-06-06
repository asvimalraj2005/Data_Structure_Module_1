# Prepend and Append 
# https://codeforces.com/problemset/problem/1791/C
# Straight forward approach 
# Below is the code 
def Problem19():
    t=int(input())
    for _ in range(t):
        n=int(input())                          # Length of the input 
        s=input()                               # Binary String 
        list_s=list(s)                          # Converting the stirng into list
        list_s.pop(0)                           # Removing the first element 
        list_s.append('1')                      # Appending '1' to the last index 
        list_s=''.join(list_s)                  # removing the quotes 
        decimal_number=int(list_s,2)            # converting the list of binary number into decimal 
        print(decimal_number)                   # Printing them onto the user's screen 
        

Problem19()
        

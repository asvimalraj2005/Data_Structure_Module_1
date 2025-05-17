# Problem Statement 
# You are given two integer A and B, Set the A-th bit and B-th bit in 0, and return iutput in decimal Number System
# Note: The bit positions are 0-indexed, which means that the least significant bit(LSB) has index 0  ----> 256  128  64  32  16  8  4  2  1 
#                                                                                                           MSB                            LSB 
# Example A=3 and B=5 ==> O/P : 40     
#                    reverse index position   6   5   4   3  2  1  0
#                            index position   0   1   2   3  4  5  6 
# Explanation by using the bit representation 64  32  16  8  4  2  1                                                                                    
# A+1 and B+1 position in the binary                                             <- The loop iteration should be started from here if you use a loop if not position based indexing then N-1-A and N-1-B 
# representation will get changed              0   1   0  1  0  0  0             => 40         
# Problem Solution Approach 
# Create a Empty List filled with zeroes with the max length by using max function by comparing the A and B 
# By using the formula N-A and N-B access those indexes in the empty list
# Convert the Empty list with the A and B index modification to the String named StringFormatVariable 
# Convert the StringFormatVariable into an integer 
# Below is the python code 
def SetBit(A,B):
    N=max(A,B)                                        # By using the max function we are finding the maximum array length if B is max then we are going to create B length array vice versa 
    N=N+1
    BinaryList=['0']*N                                # Creating the list named BinaryList with zeroes single quoted around contained in them 
    BinaryList[N-1-A]='1'                             # Accessing the Ath Position and Changing '0' to '1'      
    BinaryList[N-1-B]='1'                             # Accessing the Bth Position and Changing '1' to '0'
    StringFormatVariable=''.join(BinaryList)          # Converting the BinaryList array into an String Formay where BinaryList=['1','0','1','0','1','0','1']  ---> '1010101'
    IntegerFormatVariable=int(StringFormatVariable,2) # Again converting String binary representation to an integer
    return IntegerFormatVariable                      # Returning IntegerFormatVariable 


A=4                                                   # Finding the max between this A and B
B=7                                                   # Storing them into variable named N 
Result=SetBit(A,B)                                    # Returned result will be stored here
print(Result)                                         # Printing the result 


    
    
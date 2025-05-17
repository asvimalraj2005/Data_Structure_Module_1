# Problem Description
# You are given two integer A and B 
# -> If B-th bit in A is set, make it unset
# -> If B-th bit in A is unset, leave as it is 
# Return the updated A value 
# Problem approach 
# A will be given as any natural number 
# B is the position where we should unset the bit where it is set i.e changing 1 from to 0, if it is already 0 then leave as it is and return 
# -> By using format function we are converting A to its binary representation and storing the converted binary representation to an variable named 'C'
# -> Iterating the position B in C, and converting 1 to 0 after returing the value A by converting again into integer by using a function 
# Below is the python code for the above approach 
def Unset_ith_Bit(A,B):
    C=format(A,'b')                              # Now we are storing the converted Binary representation of A in C 
    BinaryList=list(C)                           # Now we are converting the string into list for easier finding of B position of the bit in the BinaryList and converting them 
    N=len(BinaryList)                            # Now this N stores the length of the BinaryList 
    if BinaryList[N-1-B]=='1':                   # Now this used to modify the bit -> LSB to MSB we should not go forward, move backward by using the formula N-1-B 
        BinaryList[N-1-B]='0'                    # If the position B is already filled with 1 then we should have to change it with 0 otherwise return as it is 
                                                 # After the conversion we should have again change back to it's original format that is string 
    StringFormatVariable=''.join(BinaryList)     # By using 'join' method we are converting back the list format into string and storing the list string converted format into 'StringFormatVariable'
    IntegerFormatVariable=int(StringFormatVariable,2)   # Now we are converting the string contained binary representation to its original integer format 
    return IntegerFormatVariable
                          # Index                                      0  1  2  3  4 
                          #                                           16  8  4  2  1 
A=20                      # Value A representation in bit format -->  1   0  1  0  0 
B=3                       # Now B=3                                       |  <  <  <     we are moving backward by using the formula N-1-B, the bit is already unset so we are returning the A itself
Result=Unset_ith_Bit(A,B) # Consider N=5 B=3 now subtract both of them and with -1 this become 5-1-3 = 1 is the index postion 
print(Result)                        

    
    
    
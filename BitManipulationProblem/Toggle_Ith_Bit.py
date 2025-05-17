# Problem Statement : Toggle Ith B bit in A 
# A is an natural number, B is the Position where we have toggle 
# Return the A value after toggling 
# Solution Approach for this problem -> Convert A into Binary Representation by using format function and storing them into an variable named C 
# By using BinaryList we are storing the string value in this BinaryList for easier toggle changing from this range, or an single position 
# By using B-N-1 formula we are directly accessing the Bth position in the BinaryList array if it 0 we are changing them to 1; if it is 1 we are changing them to 0 
# Below is the python code
def ToggleBit(A,B):
    C=format(A,'b')                                      # By using format function we are converting A to it's binary representation and storing them to C variable 
    BinaryList=list(C)                                   # Converting C string value to BinaryList we store the value of the string in seperate-separate comma based values for easier iteration purpose
    N=len(BinaryList)                                    # By using N we are storing length of the BinaryList 
    if BinaryList[N-1-B]=='1':                           # Accessing the Bth position if it one changing to 0
        BinaryList[N-1-B]='0'
    elif BinaryList[N-1-B]=='0':                         # Accessing the Bth position if it zero changing to 1 
        BinaryList[N-1-B]='1'   
    StringFormatVariable=''.join(BinaryList)             # Again converting the BinaryList array to String and storing into StringFormatVariable
    InterFormatVariable=int(StringFormatVariable,2)      # Again converting the String format binary representation into Integer
    return InterFormatVariable                           # Returning the Integer

                            # Index Position                0  1  2  3  4 
                            #                              16  8  4  2  1 
A=20                        # Binary representation 20 is   1  0  1  0  0     
B=1                         #                                        |  <
Result=ToggleBit(A,B)       #                               1  1  1  1  1 
print(Result)


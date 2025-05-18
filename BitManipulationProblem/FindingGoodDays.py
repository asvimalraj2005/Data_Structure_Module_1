# Problem Description 
# Alex has a cat named Boomer. He decides to put his cat to the test for eternity.He starts on day 1 with one stash of food unit, every next day, the stash doubles.
# If Boomer is well behaved during a particular day, only then she receives food worth equal to the stash produced on that day.Boomer receives a net worth of A units of food. What is the number of days she received the stash?
# Input Format : First and only argument is an integer A
# Return an integer denoting the number of days Boomer was well behaved 
# A = 5             A = 8
# Output is 2       Output is 1 
# Explanation : To eat a total of 5 units of food, Boomer behaved normally on Day 1 and on the Day 3 
# Explanation : To eat a total of 8 units of food, Boomer behaved normally only on day 4 

# Significant Bits                                                              MSB                 LSB
# Indexes                                                                       8  7  6  5  4  3  2  1   
# From the input and output with the explanation I can see that they are using  64  32  16  8  4  2  1     <--  (Used for Bit Calculation)  
#                                                  where A = 5 we can see that  0   0   0   0  1  0  1     -->  On day one and on day three -> so the count becomes 2
#                                                  where A = 8 we can see that  0   0   0   1  0  0  0     -->  On day four -> so the count becomes 1
# So the problem solving approach is convert the given number A into binary string format and store them into variable named C 
# After the conversion convert the variable C string value into BinaryList array where string value '1010101' will get converted into ['1','0','1','0','1','0','1']
# After this count the 1's present inside the BinaryList Array and return the count 
# Below is the python code for the above passage 
def GoodBehavedDays(A):
    C=format(A,'b')                     # Conversion of Integer to String binary representation happens here by using the format function 
    BinaryList=list(C)                  # Converting the C variable which stores the string binary representation is converted into list named BinaryList 
    count=0                             # Count Variable is initialised here 
    for bit in BinaryList:              # Traversing over the BinaryList array using the bit iterator 
        if bit=='1':                    # While in the process of iteration if bit == '1' then the count variable will get increased by 1 
            count=count+1
    return count                        # After that we are returning the count of bits 

A=34                                    # Example A = 34 --> Binary Representation 64  32  16  8  4  2  1 
Result=GoodBehavedDays(A)               #                                           0   1   0  0  0  1  0     count=2       
print(Result)

# Yep same concept of the basics will get applied everywhere 

# Problem statement 
# Write a function that takes an integer and returns the number of 1 bits present in it's binary representation 
# Input Format --> First and onlt argument contains integer A 
# Output Format --> Return an integer containing how many set bits are there 
def numSetBits(A):
    binaryformat=format(A,'b')                          # Converting the integer to binary by using format function and storing the value converted into 'binaryformat' variable
    Count_of_Set_Bits=0                                 # Using an counter named Count_of_Set_bits for counting the set bits 
    for bit in binaryformat:                            # Executing a loop by using bit as the iterator over the binaryformat variable 
        if bit=='1':                                        # if i=='1' then we are incrementing Count_of_Set_Bits by 1   
            Count_of_Set_Bits=Count_of_Set_Bits+1
    return Count_of_Set_Bits                            # After we are returning the Count_of_Set_Bits 


Result=numSetBits(20)
print(Result)




            
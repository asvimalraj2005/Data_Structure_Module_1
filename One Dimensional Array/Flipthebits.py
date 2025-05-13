# Binary string as input 'A'
# Flip the bits 0 -> 1 and 1 -> 0 
# Objective is to perform atmost one operation such that in the final string number of 1's is maximized
# Below is the entire explanation how the flipping work
# Here we didn't use the kadane algorithm, if it is being currently used then we can easily solve the question without using two loops instead with two pointers 
# Below is the function which takes string as the parameter
# The output is to return the two indexes where the no of 1's in between them is get maximised after flipping.
# Example one consider '1001' and '0100'
#       1001                   0100
#       1001 -> 0001           0100 -> 1100             --> 1           2         
#       1001 -> 0101           0100 -> 1000             --> 2           1             
#       1001 -> 0111           0100 -> 1010             --> 3           2          <-- for example 1 we can see that maximum 1's after flipping from j to n is 3 
#       1001 -> 0110           0100 -> 1011             --> 2           3          <-- for example 2 we can see that maximum 1's after flipping from j to n is 3 
# We should return the indexes from the start to end without affecting the outer loop 
# Below is the example for all of those 


def flip(A):                                                            # Passing down the String consisted of 1's and 0's 
    empty_list=[]                                                       # Creating an empty list which is going to store the string                                                       
    empty_list=list(A)                                                  # Converting them to list where it will get stored as from this '11111' to this ['1','1','1','1','1']                                                 
    answer_list=[]                                                      # Creating an empty list for storing the both the indexes where the max flipped 1's stays
    n=len(A)                                                            # creating a length variable n to store the length of the string                                                
    max_gain = 0                                                        # Dummy variable used for calculating purpose
    for i in range(n):                                                  # Entering the loop -> This loop will run from start of the index to end index of the list 
        count_var=0                                                     # Initialising the count variable which will automatically restores or resets to 0 after the calculation of the inner loop which runs from i,n 
        for j in range(i,n):                                            # Same as above j runs i,n with counting variable named as count_var 
            element_j=empty_list[j]                                     # Accessing the list element by using the element_j variable 
            if element_j=='0':                                          # If element_j is equals to '0' we are making the count_var to add 1 to it because we are stimulating as it was get changed but it doesn't and counted i.e if elememt_j=='0' then it will be viewed as element_j=='1' and count_var adds one to it 
                count_var=count_var+1                                   
            if element_j=='1':                                          # If element_j is equals to '1' we are making the count_var to add o to it because if is 1 -> 0, so making them counted is an unnecessary one 
                count_var=count_var+0
            if count_var>max_gain:                                      # Using the max_gain global variable as a dump variable inside the inner loop to validate the condition for the count_var if so the count_var is greater than the max_gain then the below process will get held on for every loop iteration 
                max_gain=count_var                                      # Here the max_gain is updated with the value of count_var 
                answer_list=[i+1,j+1]                                   # Answer is also being updated with the indexes i+1 and j+1 
            elif count_var == max_gain and answer_list and [i + 1, j + 1] < answer_list:   # This condition is used to check if the count_var which is used to count the flips is equal to max gain -> this says after the updation of max_gain and answer_list we are finding a new indexes which has maximum ones in them and the newly updated indexes i+1 and j+1 should be lesser than < answer_list : the index i must be smaller and index j should be greater then before 
                    if [i + 1, j + 1] < answer_list:                    
                        answer_list = [i + 1, j + 1]
    return answer_list                                                  # Returning the answer_list 


result=flip('101010')
print(result)
                    
# Problem statement 
# Given an array with N objects coloured red , white , or blue, sort them so that objecs of the 
# same color are adjacent, with the colors in the order red, white, and blue 
# we will represent the colors as, 
# red --> 0
# white --> 1 
# blue --> 2 
# Note : Using the library sort function is not allowed 
# Input Format : First and only argument of input contains an integer array A 
# Output Format : Return an integer array in asked order 
# 
# Example with explanation 
# Input --> A = [ 0 , 1 , 2 , 0 , 1 , 2 ]
# Output --> [ 0 , 0 , 1 , 1 , 2 , 2 ]
# red red white white blue blue the numbers are organised in the manner 
#
# In interviews just use sort function for sorting all the elements in the array but if the interviewer not to use any sorting function just create your own method and sort the array in ascending order, code it 
# There are several algorithm that are publicly available same approach but with desing code designs that are used to sort the array 
# Below is the code for the above approach 
# 
def Sort_by_Color(A):
    
    # Approach 1 that I have found easy use sort()
    # return A.sort()                                         <--- Single line solution 
    
    # Approach 2 use any of the sorting algorithm ( in-place with out changing the order or non-in-place algorithms with changes the order of the equal elements but usually it returns the sorted array )
    # Selection sort() , Merge Sort() , Insertion Sort() , Quick Sort(), Bubble Sort(), Heap Sort() etc what ever you prefer or by using two pointer you can sort the array 
    # Below is the approach I have chosen 
    # Selection Sort 
    
    #N=len(A)                                                 <--- Approach 2 
    #for i in range(N-1):                            
    #    min_ind=i                                   
    #    for j in range(i+1,N):                      
    #       if A[j]<A[min_ind]:                    
    #            min_ind=j                          
    #    A[i],A[min_ind]=A[min_ind],A[i]            
    #return A  
    
    pass    


A=[0,1,1,0,0,1,2,1,0,1,2,1]
print(Sort_by_Color)

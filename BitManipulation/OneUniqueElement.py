# Problem Statement 
# Given arr[N] where every element is present twice except one unique element. Find that unique element 
# The main approach is used here XOR method 
#   Property 7 
#
#   A ^ A                         A = S --> 1 0 1 
#                                     ^     
#                                           1 0 1 
#                                           0 0 0  --> 0      
#
# Same elements XORED with same element once when in iterating gives the answer as 0 
# Below is the python code 
#
def UniqueElements(Arr):
    ans=Arr[0]                              # Storing the first element of the given array on ans variable 
    N=len(Arr)                              # Storing the len of the variable in N
    for i in range(1,N):                    # Executing the loop from 1 to N-1
        ans=ans^Arr[i]                      # Using the approach if the index 0 element is as index 1 element then the ans=0 if the index 1 is unique from overall index elements then overall elements in the array then index 1 element is the array if not the array elements present twice then the ans=0 
    return ans                              # Returning the answer 
#
#
Arr=[1,2,2,3,3,4,4,5,5,6,6,7,7]
print(UniqueElements(Arr))       # Output = 1
#
#
Arr=[2,2,3,3,4,4,5,5,6,6,7,8,8]
print(UniqueElements(Arr))       # Output = 7 *
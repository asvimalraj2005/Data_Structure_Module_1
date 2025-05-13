#Given arr[N]. Find the maximum subarray sum out of all subarrays
# arr[] -> [-3,2,4,-1,3,-4,3]
#              ________        2+4+-1+3=8
# arr[] -> [4,5,2,1,6]
#           __________         4+5+2+1+6=18
#Bruteforce -> For all subarrays. Calculate sum and take max 
#                 N*(N+1)/2       iterate all subarrays TC=O(N^3)
# When all elements are positive ; sum all the elements 
# When all elements are negative ; max(A[i])
# when the left side is negative, mid is positive and the left side is negative 
# Using Kadane's algo given an array where arr[] is [5,6,7,-3,2,-10,-12,8,12,-4,7,-2]
# Sum                                                5 11 18 15 17 7 -5 8 20 16 23 21 
# ans                               max              5 11 18              
# Sum                                                                Here -5 becomes 0 so we start a new sum from this element 
# The code 
def Kadanes_algorithm(arr):
    sum_var=0
    ans=arr[0]
    for i in range(len(arr)-1):
        sum_var=sum_var+arr[i]
        ans=max(sum_var,ans)
        if sum_var<0:
            sum_var=0
    return ans

arr=[5,6,7,-3,2,-10,-12,8,12,-4,7,-2]
result_var=Kadanes_algorithm(arr)
print(result_var)


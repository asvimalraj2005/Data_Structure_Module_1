# Given arr[N], where arr[i] -> height of the building 
# Return amount of water trapped on all the buildings   1<=N<=20^5
# width=1 for all buildings 
# Find the amount of water trapped on every building 
# max A[i] on left 
# max A[i] on right        Left boundary   }   _   {   Right boundary 
# h=min(left[i],right[i])-A[i]
# w=1    area=h*1=h
#   arr=[2,1,3,2,1,2,4,3,2,1,3,1]
#  left=[2,2,3,3,3,3,4,4,4,4,4,4]
# right=[4,4,4,4,4,4,4,3,3,3,3,1]
# water=[0,1,0,1,2,1,0,0,1,2,0,0]
# Ans=     1   1 2 1     1 2    -> 8 
def rain_water_trapping(arr):
    
    n=len(arr)
    
    left=[0]*n
    right=[0]*n
    
    left[0]=arr[0]
    for i in range(1,n):
        left[i]=max(left[i-1],arr[i])
    
    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],arr[i])
    
    ans=0
    for i in range(len(arr)-1):
        water=min(left[i],right[i])-arr[i]
        if water>0:
            ans=ans+water
    return ans
arr=[2,1,3,2,1,2,4,3,2,1,3,1]
print(rain_water_trapping(arr))



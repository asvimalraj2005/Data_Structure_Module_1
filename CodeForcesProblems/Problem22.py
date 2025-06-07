# Arrays 
# https://codeforces.com/problemset/problem/572/A
# Below is the code for the above problem
def Problem22():
    A,B=map(int,input().split())                        # Length of the Array A and Array B 
    K,M=map(int,input().split())                        # K number you can choose from the array A and M numbers you can choose from the array B   
    Array_A=list(map(int,input().split()))              # Space separated numbers converted to an Array 
    Array_B=list(map(int,input().split()))              # Space separated numbers converted to an Array 
    # The K numbers should be less than M number so for this list slicing will be used  
    # Condition check if K and M is not less than or equal to  A and B we are exiting from the function 
    if K<=A:
        list_slice_A=Array_A[:K]
    if M<=B:
        list_slice_B=Array_B[:M]
    Greater=False
    for i in range(len(list_slice_B)):
        b_array_element=list_slice_B[i]
        for j in range(len(list_slice_A)):
            a_array_element=list_slice_A[j]
            if a_array_element>=b_array_element:
                Greater=True
                print("No")
                break
        if Greater:
            break
    if not Greater:
        print("YES")
   

Problem22()
    
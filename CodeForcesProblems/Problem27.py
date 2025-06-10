# https://codeforces.com/problemset/problem/1398/C
# Below is the code for the above problem statement link
def Problem27():
    t=int(input())
    for _ in range(t):
        n=int(input())          # <- Length of the array 
        s=input()
        num_array=list(map(s.split()))
        print(num_array)
       
        index_var=0
        count=0
        for i in range(len(num_array)):
            for n in range(i,len(num_array)):
                sum_var=0
                for m in range(i,n):
                    sum_var=sum_var+num_array[m]
                    index_var=index_var+m
                if sum_var==index_var:
                    count=count+1
    print(count)

Problem27()                                                         # The above code is implemented by me 

                                       
# Online referrence code 

def Problem27():
    t = int(input())
    for _ in range(t):
        n = int(input())          # <- Length of the array 
        s = input()
        num_array = [int(digit) for digit in s] 
        count = 0       
        for l in range(n):                              # Outer loop: 'l' for the starting index of the subarray
            for r in range(l, n):                       # Inner loop: 'r' for the ending index of the subarray
                sum_var = 0  # Reset sum for each new subarray
                # Calculate sum of elements from index l to r
                for m in range(l, r + 1): # Iterate from l to r (inclusive)
                    sum_var += num_array[m]
                # Calculate the length of the subarray (r - l + 1)
                length_var = r - l + 1 
                # Check if the sum equals the length
                if sum_var == length_var:
                    count += 1
        print(count)

Problem27()                

        
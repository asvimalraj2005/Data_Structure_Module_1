# Make Even 
# https://codeforces.com/problemset/problem/1611/A                    
# Below is the code for the above problem statement 
def Problem22():
    t=int(input())
    for _ in range(t):
        n=int(input())
        if n%2==0:
            print(1)
        else:
            input_list=list(str(n))
            count=0
            remove_index=1
            Even=False
            while(n%2==0):
                element_index=input_list[remove_index]
                input_list.pop(remove_index)
                input_list.insert(0,element_index)
                element_index=element_index+1
                count=count+1
                n=int(''.join(map(str,input_list)))
                Even=True
                break
            if Even:
                print(1)
    if not Even:
        print(-1)           # Original code syntatic error 
        



# Online reference 

def Problem22():
    t = int(input())
    for _ in range(t):
        n = int(input())
        input_list = list(str(n))                   # convert int to list of digit characters
        count = 0
        found_even = False

                                                    # Case 1: already even
        if int(input_list[-1]) % 2 == 0:
            print(0)
            continue

                                                    # Try moving each digit to the front one by one
        for i in range(len(input_list)):
            if int(input_list[i]) % 2 == 0:
                                                    # move digit at position i to the front
                digit = input_list.pop(i)
                input_list.insert(0, digit)
                count += 1

                                                    # recreate the new number
                new_n = int(''.join(input_list))

                                                    # check if new number is even
                if new_n % 2 == 0:
                    found_even = True
                    break
                else:
                                                    # if not even, revert and try next
                    input_list.pop(0)
                    input_list.insert(i, digit)
                    count = 0                       # reset count

        if found_even:
            print(count)
        else:
            print(-1)

                
                
                
               
            
        

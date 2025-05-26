# Hash map implementation just on my own with out anty tutorial but with using list and passing the elements to the list which are going to be stored in the calculated index by using the hash function
# Not by using a class but using function in basic way to know the approach
# Create a list named 'HashMap' within a function named Storage         <--- Storage is used to store the values passed by the user
# Create a Function named Hash_Index                                    <--- Hash_Index function is used to calculate the index inside the list where the value is going to be stored, I know same values create collision but for now limited unique numbers 
# Create a function named Retrieve_Value                                <--- Retrieve_value function is used to get the stored value to the user 
# Create a function named Store_Value                                   <--- Store_value function is used to store the value inside the list 


def Storage(Element,Index):
    List=[]
    N=len(List)
    if Index==None:
        return 
    Containment_Check=List.get(List[Index])
    if Containment_Check==None:
        List[Index]=Element

def Hash_Index(N,Element):
    index=Element%N
    return index

def retrieve(Element):
    retrieve_index=Hash_Index(Element)
    retrieve_storage=Storage(Element,retrieve_index)
    print(retrieve_storage)
    
def store_value(Element):
    hash_index=Hash_Index(Element) 
    
# Above Implemented code is wrong 
# Below is the code for implementation of hashmap without the usage of classes 

hash_table = [None] * 10 

def hash_index(element):                                                            # Function is used for calculating the hash table indexes 
    return element % len(hash_table) 
def store_value(element):
    index = hash_index(element)                                                     # To store the element first its index is calculated 
    if hash_table[index] is None:                                                   # If the index is None then we are eligible to store that index 
        hash_table[index] = element                                                 # storing the element on that index 
    else:
        print(f"Collision detected at index {index} for element {element}!")        # If the index is full then collision is happened 
def retrieve(element):                                                              # Function for retrieving the element 
    index = hash_index(element)                                                     # First getting the index of that element 
    if hash_table[index] == element:                                                # If the element in the hash_table is same as the element we have in the retrieve function then the same element will be returned if not None is returned 
        return element
    else:
        return None

store_value(12)  
store_value(22)  
print(retrieve(12))  
print(retrieve(22))
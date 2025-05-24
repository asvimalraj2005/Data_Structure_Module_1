<<<<<<< HEAD
# Hash Map Introduction 
# It is an index based data structure 
# We can able to calculate the index of the element value by using the same element value and by using hash function 
# That is think of an array consisting of numbers [ 1 , 2 , 3 , 4 , 5 , 1 ]
# where to calculate the index we should to use the hash function and an empty list or an data structure which is used to store the element in the calculated index 
# Various function will get involved mainly for storing, retrieving, calculating the index, deleting the value etc
# Explanation [ 1 , 2 , 3 , 4 , 5 , 1 ]
# To calculate the index of an variable we are going to divide the key with table_size -> now this gives the index 
# empty_array = []      <----- now at this position the element which is used to calculate the index will be stored in here 
# Unique elements in the list does not creates any collision 
# whereas if the array is consist of same elements then the hash function will provide the same indexes for the element, this causes an collision between the positions and no more than one elements is stored in the position, if you want store multiple elements in that same posistion you can use chaining method, 
# chaining create a sub list inside that position like [ 1 , [ 2 , 3 ] , 4, 5 , 6 ,0 ]
# Use linear probing etc many methods which are related to collision handling are available 
=======
# Hash Map Introduction 
# It is an index based data structure 
# We can able to calculate the index of the element value by using the same element value and by using hash function 
# That is think of an array consisting of numbers [ 1 , 2 , 3 , 4 , 5 , 1 ]
# where to calculate the index we should to use the hash function and an empty list or an data structure which is used to store the element in the calculated index 
# Various function will get involved mainly for storing, retrieving, calculating the index, deleting the value etc
# Explanation [ 1 , 2 , 3 , 4 , 5 , 1 ]
# To calculate the index of an variable we are going to divide the key with table_size -> now this gives the index 
# empty_array = []      <----- now at this position the element which is used to calculate the index will be stored in here 
# Unique elements in the list does not creates any collision 
# whereas if the array is consist of same elements then the hash function will provide the same indexes for the element, this causes an collision between the positions and no more than one elements is stored in the position, if you want store multiple elements in that same posistion you can use chaining method, 
# chaining create a sub list inside that position like [ 1 , [ 2 , 3 ] , 4, 5 , 6 ,0 ]
# Use linear probing etc many methods which are related to collision handling are available 
>>>>>>> 04bbde135af7bd24cf307d36f1101db4b5ba49dd

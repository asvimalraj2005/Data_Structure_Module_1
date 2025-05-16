# Even / Odd Number ->
#                           Most Significant Bit                  Least Significant Bit                   Most Significant Bit  
#      11           ->               1         0         1           1  
#      &
#      1                             0         0         0           1
#      Answer       ->               0         0         0           1                                  
#
#
#
#                            Most Significant Bit                  Least Significant Bit                  
#      10           ->               1         0         1           0 
#      &
#      1                             0         0         0           1
#      Answer       ->               0         0         0           0
#
#      Odd   -> Least Significant Bit is always 1
#      Even  -> Least Significant Bit is always 0        
#
#      A & 1 -> 1 => A is odd
#            -> 0 => A is even 
#
#     Property 2
#
#     A & 0  -> 0                 A = S --> 1 0 1
#                                     &    
#                                     0     0 0 0
#                                           0 0 0  --> 0
#
#     Property 3
#
#     A & A  -> A                A = S --> 1 0 1 
#                                    &
#                                    A     1 0 1 
#                                          1 0 1   --> 5
#
#    Property 4 
#
#    A || 0  -> A                 A = S --> 1 0 1
#                                    ||  
#                                     0     0 0 0
#                                           1 0 1  --> 5 
#
#    Property 5 
#
#    A || A -> A                  A = S --> 1 0 1 
#                                    || 
#                                     A     1 0 1 
#                                           1 0 1  --> 5
#
#    Property 6                  
#
#    A ^ 0 -> A                   A = S --> 1 0 1 
#                                     ^
#                                           0 0 0
#                                           1 0 1  --> 5
#
#   Property 7 
#
#   A ^ A                         A = S --> 1 0 1 
#                                     ^     
#                                           1 0 1 
#                                           0 0 0  --> 0
#
#
#   Cumulative Property -> Order of operands don't matter 
#
#                                 A & B = B & A
#                                 A | B = B | A 
#                                 A ^ B = B ^ A 
#
#   Associative Property -> Grouping of operands don't matter 
#                                   
#                                 (A&B)&C = A&(B&C)
#                                 (A|B)}C = A|(B|C)
#                                 (A^B)^C = A^(B^C)


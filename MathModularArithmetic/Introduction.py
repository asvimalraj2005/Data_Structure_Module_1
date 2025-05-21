# An Introduction about modulo 
# Modulo % Operator 
# A % B => Remainder when A is divided by B 
# Range of A % B => [ 0 B-1]    --> ans % ( 10 ^ 9  +  7 )
# 10 % 3 = 1  and  0 < = x % 3 < = 2  or  5 % 8 = 5 
#
# if ( A < B ) => A % B = A 
# 
# Modular Arithmetic ( Below  are  the  formula  used  for  calculation  in  multiple  diciplinaries)
# 
# 1) ( a + b ) % m = ( ( a % m ) + ( b % m ) ) % m 
# Eg : a = 9 , b = 8 , m = 5  ( can store value < 10 )
# ( 9 + 8 ) % 5 => 17 % 5 => 2
# a % m => 9 % 5 = 4 
# b % m => 8 % 5 = 3          =>  ( 4 + 3 ) % 5 => 7 % 5 => 2 
#
# 
# 2) ( a + b ) % m = ( ( a % m ) * ( b % m ) ) % m
#
# 3) ( a + m ) % m = ( ( a % m ) + ( m % m ) ) % m = a % m
#
# 4) ( a - b ) % m = (( a % m ) ) - ( b %  m ) + m ) % m
# 
# Eg --> a = 7 , b = 10 , m = 5 
#
# ( a - b ) % m = ( 7 - 10 ) % 5 = - 3 % 5  -> C programming and other languages the O/P is -3
#                                           -> In python the O/P is 2 
#
# 0 - ( m -1 ) + m  = 1
# ( ( a % m ) - ( b % m ) + m ) % m  
#    _________________________  >= 0
#
# 5) ( a ^ b ) % m = ( ( a % m ) ^ b ) % m
#
#
# Q --> (37^103 - 1)%12
# => ((37 ^ 103 ) % 12 - ( 1 % 12 ) + 12 ) % 12
#     |---------------------------------------------------> (37 % 12) ^ 103 % 12
#                                                         |---------------------->  1 ^ 103 % 12 = 1 % 12 = 1
# => ( 1 - 1 + 12 ) % 12 = 12 % 12 = 0 (Ans)

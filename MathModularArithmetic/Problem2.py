# Properties of Greatest Common Divisor ( Important Formulae )
# 
# 1) gcd(a,b) = gcd ( b, a )       
#
# 2) gcd(0,a) = a 
#
# 3) gcd(a,b,c) = gcd ( a , gcd ( b , c ) )
#               = gcd ( b , gcd ( a , c ) )
#               = gcd ( c , gcd ( a , b ) )
#
# 4) gcd(a-b,b) = gcd(a,b) 
# a > = b 
#
# To prove the above -> let gcd ( a , b ) = d  --> a % d = 0
#                                              --> b % d = 0 => ( a - b ) % d =0
#                    -> let gcd ( a - b , b )  --> t => ( a - b ) % t = 0
#                                                        b % t = 0
#                                                       ( a - b + b ) % t = 0 --> a % t => 0 
#
# d is common factor of ( a - b ) & b
# --> t is gcd ( a - b , b ) => " t > = d "       -------> 
#                                                                      t = d 
# t is common factor of a & b                              
# --> d is gcd ( a , b ) => " d > = t "           -------> 
# 
# 5) gcd ( a , b ) = gcd ( a - b , b ) = gcd ( a - 2 b , b)
#                  = gcd ( a - 3 b , b )
#                  = gcd ( a % b , b )
#                  Repeated subtraction of b till value is < b
#                  => % b 
#
# gcd ( a , b ) = gcd ( a % b , b ) = gcd ( b , a % b )
# gcd ( 6 ,75 ) = gcd ( 75 , 6 % 75 = 6 )
# gcd ( 3 , 6 % 3 = 0 ) = 3 
# 
# Below is the python code for the calculating the Greatest Common Divisor by using recursion 
# 
def GCD(A,B):
    if B==0:
        return A
    else:
        return GCD(B,A%B)
    
A=2345678
B=456687348523856
print(GCD(A,B))



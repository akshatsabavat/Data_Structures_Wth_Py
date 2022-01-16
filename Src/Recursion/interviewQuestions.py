"""Question1 : Find the sum of digits in a given positive integer number(Recursion)
   For example: 10 = 1 + 0, 54 = 5 + 4, 112 = 11 + 2 = 1 + 1 + 2
   
    Solution1 : If we divide a number by 10 we will get a split of the two numbers given that we return an integer variable
               like 54/10 Reminder = 4 and quotient = 5 similarly 112/10 will give Q = 11 and R = 2, Hence we keep recursively 
               calling the f(n) = n%10 + f(n/10) with a base case of n == 0 return 0"""
    
def sumOfDigits(n):
    assert n >=0 and int(n) == n, 'The number must be a positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(139))
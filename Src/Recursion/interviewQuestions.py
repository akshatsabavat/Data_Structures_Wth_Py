"""Question 1 : Find the sum of digits in a given positive integer number(Recursion)
   For example: 10 = 1 + 0, 54 = 5 + 4, 112 = 11 + 2 = 1 + 1 + 2
   
    Logic 1 : If we divide a number by 10 we will get a split of the two numbers given that we return an integer variable
               like 54/10 Reminder = 4 and quotient = 5 similarly 112/10 will give Q = 11 and R = 2, Hence we keep recursively 
               calling the f(n) = n%10 + f(n/10) with a base case of n == 0 return 0
               whole idea is to keep addind the reminders and recursivly call the remaining numbers divided by 10"""
    
def sumOfDigits(n):
    assert n >=0 and int(n) == n, 'The number must be a positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(139))

"""Question 2: Find Power of a number using recursion (Note: Ensure the exponent is a positive integer)
   
   Logic 2: Taking a look at x^y x being an integer and y being the power its further broken down in the following way
              x^y = x * x^(y-1)
              x^y = x * x * x^(y-2)
              x^y = x * x * x * x^(y-3) ... and so on
              hence we can make a recursive call of f(x,n) = x * f(x,n-1) --Base Case: n == 1 -> n and n == 0 -> 1"""

def powerOfNumber(x,n):
    assert n >= 0 and int(n) == n, "The exponent is a positive integer"
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * powerOfNumber(x,n-1)

print(powerOfNumber(x = 12, n = 3))

"""Question 3: Convert Decimal to Binary using recursion (Number should be an integer)

   Logic 3: Decimal to Binary involves printing all the reminders in a reverse order Hence, keep dividing the subsequent quotient with 2 and then store the
            reminder, After the recursive calls have been passed, go back through the recursive tree and employ the print function"""

def decimalToBinary(n):
    assert int(n) == n, "Only integer numbers allowed"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(13))
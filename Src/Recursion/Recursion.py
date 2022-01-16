# Russian Doll code
import sys
sys.setrecursionlimit(10000) # sets recursion limit

"""
 *NOTES*

 --When to use Recursion ?
 1 ) When problem can be broken into many sub problems reducing its complexicity
 2 ) When we are fine with extra space (both time and space) that comes with it
 3 ) When we need a quick solution rather than a efficient one (Itev code is more efficient than recursion)
 4 ) Tree traversals are all done via recursion --Post Pre and In orders
 
 --When to avoid Recursion ?
 1 ) if time and space complexity are prioritized
 2 ) Recursion takes more memory, If we use an application then the recursive code of the computation can 
     take up a lot of cache or memory space on the phone
 3 ) Recursion can be slow in comparison to iteration


"""


from gettext import find


def openRussianDoll(doll):
    if doll == 0:
        print("All dolls are now opened")
    else:
        print(f"Opened doll number {doll}")
        openRussianDoll(doll - 1)

openRussianDoll(10)

def recursiveMethod_Reduction(r_Number):
    if r_Number < 1:
        print("The current number is less than 1")
    else:
        recursiveMethod_Reduction(r_Number - 1)
        print(r_Number)

recursiveMethod_Reduction(5)

def toThePower_Rec(var_Power, var_Number):
    if var_Power == 0:
        return 1
    elif var_Power == 1:
        return var_Number
    else:
        return (var_Number * toThePower_Rec(var_Power - 1, var_Number))

numberSub_Rec : int = 3
powerOf5_Rec : int = toThePower_Rec(5,numberSub_Rec)
print(powerOf5_Rec)

def findFactorial(n):
    assert n >=0 and int(n) == n, 'Makes sure the number is positive and an integer'
    # if n == 1:
    #     return 1
    # elif n == 0:  
    if n in [0,1]: # cleaner code only in python
        return 1
    else:
        return n * findFactorial(n - 1)

print(findFactorial(10))

def fibonnaciOfNumber(n):
    assert n >= 0 and int(n) == n
    if n in [0,1]:
        return n
    else:
        return fibonnaciOfNumber(n-1) + fibonnaciOfNumber(n-2)
    
print(fibonnaciOfNumber(-1))
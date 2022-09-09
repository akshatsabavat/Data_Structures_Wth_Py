#Q1. find a missing number in the list containing numbers from 1 to 10
from multiprocessing.sharedctypes import Value
from unittest import result


First_Prob_List = [1,2,3,4,5,6,7,8,9,10]

def findMissing(listTBC):
    list_Lenght = len(listTBC)
    for i in range(0,list_Lenght - 1):
        if listTBC[i + 1] - listTBC[i] != 1:
            return "{} is missing from the list".format(listTBC[i] + 1)
    return "all numbers in list"

# result = findMissing(prob_List)
# print(result)

#Q2. find the number of pairs who's sum is equal to the given number
#note if i = j --> (i,j) are not valid pairs
Second_Prob_List = [2,7,11,15,-2,-6]
target = 9

def findSumPair(listTBC, targetValue):
    satisfied_pairs = 0
    list_lenght = len(listTBC)
    for i in range(0,list_lenght - 1):
        for j in range(i + 1,list_lenght - 1): #i+1 to avoid i = j invalid pair situation
            if listTBC[i] + listTBC[j] == targetValue:
                satisfied_pairs = satisfied_pairs + 1
    return satisfied_pairs

# result = findSumPair(Second_Prob_List, 9)
# print(result)

#Q3. Find the max product of two numbers in the array
Third_Prob_List = [2,7,11,15,-2,-6]

def maxProduct(listTBC):
    list_Lenght = len(listTBC)
    maxProduct = 0

    for i in range(list_Lenght):
        for j in range(i+1,list_Lenght):
            if listTBC[i] * listTBC[j] > maxProduct:
                maxProduct = listTBC[i] * listTBC[j]
                maxProduct_pairs = str(listTBC[i]) + "," + str(listTBC[j])
    print(maxProduct_pairs)

#maxProduct(Third_Prob_List);

#Q4. Check if each element in the given list is unique or not
good_Array = [10,22,1,3,4,6,7,9,45]
bad_Array = [90,2,3,4,10,11,6,7,90]

def checkUnique(listTBC):
    string = "array is unique"
    a = []
    for i in range(len(listTBC)):
        if listTBC[i] in a:
            string = "array contains a duplicate for {}".format(listTBC[i])
        else:
            a.append(listTBC[i])
    print(string)

checkUnique(good_Array)
checkUnique(bad_Array)

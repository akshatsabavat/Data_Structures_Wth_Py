#data structure that holds a collection of items
#can store integers, strings, floats ect..
#can also have a collection of all types

#int type
from multiprocessing.managers import ListProxy
from socket import inet_aton
from tabnanny import check


integers = [10,11,9,10]

#string type
strings = ['Eddy','Jhon','Karl']

#string + float + integer
strings_and_integers = ["eddy",11,19,55.6,"Edmond"]

print(strings_and_integers)

#accessing list elemenst
print(integers[1])
print(integers[2])
sum = integers[1] + integers[2]
print(sum)

#checking for values --> returns either true of false
check = 11 in integers
checkTwo = 12 in integers
print(check) #true condition
print(checkTwo) #false condition

#sum of all elements in list
def listSum(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum + integers[i]
    print(sum)

listSum(integers)
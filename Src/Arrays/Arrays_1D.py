from array import * #imports an array module

arrayOne = array('i', [1,2,3,4,5,6]) # 'i' specifies only integer values
arrayTwo = array('d', [1.2,2.0,1.9,3.5]) # 'd' specifies only double values

print(arrayOne,arrayTwo)

arrayOne.insert(2,8) # first argument specifies where to insert and second argument specifies what to insert
print(arrayOne)

#Time complexity for inserting array element is O(n) as we need to shit the other remaining elements and make space
# Time complexity for inserting at the end of the array is O(1) --Constant array as we inser at the last no shifts required

# Code to traverse the array
# Time complexity is O(n)
# Space complexity is O(1)

def traverseArray(arr):
    for i in arr:
        print(i)

traverseArray(arrayOne)
traverseArray(arrayTwo)

# Code for accessing the array

def accessElement(array, index):
    assert index < len(array), "Lenght greater than array"
    print(array[index])

accessElement(arrayTwo, 1)
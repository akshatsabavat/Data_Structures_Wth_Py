from ctypes import pointer


class Node: #class to define the node of a linked list
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList: #class to define the head pointer/ structure of a singly linked list
    def __init__(self):
        self.head = None
        self.tail =  None

def createList(self, value):
    newNode = Node(value)
    if self.head == None:
        self.head = newNode
        self.tail = newNode
    else:
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = newNode
    return self.head

def printList(self):
    ptr = self.head
    while ptr.next != None:
        print(ptr.value)
        ptr = ptr.next

__author__ = "Abhishek S Shinde"
__copyright__ = "EXDAS"
__contact__ = "arabhishek1091@gmail.com"

"""
Refer to Example of the linkedlist is in linkedList.py
and then follow this example
The process of printing Next Available node in a LinkedList is Tedious especially
when you want to print out more than 1000.. values of nodes .
In that case, you need to use traversing technique(a function with While Loop or iter)

"""
#Step1- Defining a class Node
class Node:
    def __init__(self,value):
        self.value = self
        self.next = None


#Step 2 - Defining values for the head Node and consecutive Nodes w.r.t head node
head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)
        
#Step2- Defining a Function for Traversing a LinkedList and Printing values independent of the length of List
def traverseLinkedList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.value)
        #Returning the value in the function
        currentNode = currentNode.next
        
        
#Step3 - Calling the function for travering the List
traverseLinkedList(head)


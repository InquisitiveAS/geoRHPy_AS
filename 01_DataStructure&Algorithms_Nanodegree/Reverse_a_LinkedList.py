
#Creating a class Node
#This class points to the input data as the value of the node using __init__() definition
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#Reversing a LinkedList
"""
1)Iterate through the List
2)Swap the 'next' pointers of each node
3)Do steps 1) and 2) using a reverse() method
"""
#Creating a LinkedList for the Node
class LinkedList:
    def __init__(self):
        self.head = None
        
    def reverse(self):
        #Specify the current node
        current = self.head
        #Specify the previous node
        previous = None
        #Specify the next node
        next = None
        
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous

#Here we initialize class Linked List
abhis_linkedlist = LinkedList()
#Creating the head value of the newly intialized Linked List class using Node class
#This will create a Head Node with a value of 1
#Note : node_1 = abhise_linkedlist.head = 1
abhis_linkedlist.head  = Node(1)
print("Print the head of the linkedlist when initialized:")
print(abhis_linkedlist.head)
#Creating two more additional nodes as requested
node_2 = Node(2)
node_3 = Node(3)
#Declaring the node next to the head as node_2
abhis_linkedlist.head.next = node_2
#Declaring the node next to the node_2 as node_3
node_2.next = node_3

#Reversing the linkedlist 
abhis_linkedlist.reverse()
print("Print the head of the linkedlist after reverse():")
print(abhis_linkedlist.head)


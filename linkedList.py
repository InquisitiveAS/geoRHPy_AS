__author__ = "Abhishek S Shinde"
__copyright__ = "EXDAS"
__contact__ = "arabhishek1091@gmail.com"

"""
Simple Linked List
The Linked List are referenced to each other with attribute "next"
class Node is used to demonstrate a Simple Linked List
All values in Linked List are referenced with "head" 
These values are not in sequence and can be located anywhere
This data Structure is useful than arrays 
    
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

#print(head.next) will print a pointer to the address where the object is stored
#<__main__.Node object at 0x7f2c2b16f5f8>
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
print(head.next.next.next.next.next.value)

"""
The above process is Tedious when you want to print out more than 1000.. values of nodes
In that case, you need to print use traversing technique using While Loop or iter
    
"""

class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def push(self, new_data):
       """Adds new node to the beginning of list"""
       #creating new node
       new_node = Node(new_data)
       #moving beginning of list forward
       new_node.next = self.head
       #putting new node to the begginh of list
       self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        """Adding new node after a specific node in list"""
        if prev_node is None:
            print('Node does not exists! ')
            return
        #Adding new node 
        new_node = Node(new_data)
        #Conneting new node to next node
        new_node.next = prev_node.next
        #Connedting previous node to new node 
        prev_node.next = new_node
    
    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def deleteNode(self, key):
        temp = self.head
        if (temp and temp.data == key):
            self.head = temp.next
            temp = Node
            return
        while temp:
            if temp.data == key:
                break
            prev = temp.next
            temp = temp.next
        if temp == None:
            return
        prev.next = None
        temp = None
        
     
       

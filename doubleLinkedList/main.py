class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class doubleLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        '''
        This method append a node at the end of the linked list
        '''
        if self.head==None and self.tail==None: #check if nodes in the list
            new_node=Node(data)  #create new node
            self.head=self.tail=new_node #point tail and head pointers to the new node
        else:
            new_node=Node(data)  #create new node
            self.tail.next=new_node #point tail next to the new node
            new_node.previous=self.tail #point previous of new node to the last node
            self.tail=new_node #move the pointer to the new node

    def prependNode(self,data):
        '''
        This method append a node a the beggining of the linked list
        '''
        if self.tail==None and self.head==None: #check if nodes in linked list
            new_node=Node(data)  #create new node
            self.tail=self.head=new_node #assign pointers head and tail to the new node
        else:
            new_node=Node(data) #create new node
            new_node.next=self.head # point the next node of the new node to the previous head
            self.head.previos=new_node #point the previos head previous to the new node
            self.head=new_node #move the pointer head to the new node
        
    def printNodesFromHead(self):
        '''
        This method prints the nodes in the linked list
        '''
        print("Print nodes strating at the head")
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

    def printNodesFromTail(self):
        '''
        This method prints the nodes starting from the end
        '''
        print("Print nodes starting at the tail")
        cur=self.tail
        while cur:
            print(cur.data)
            cur=cur.previous

if __name__=="__main__":
    doubleLinkedListObj=doubleLinkedList()
    doubleLinkedListObj.append(19)
    doubleLinkedListObj.append(3)
    doubleLinkedListObj.append(1)
    doubleLinkedListObj.printNodesFromHead()
    doubleLinkedListObj.printNodesFromTail()
    doubleLinkedListObj.prependNode(90)
    doubleLinkedListObj.prependNode(38)
    doubleLinkedListObj.printNodesFromHead()

    





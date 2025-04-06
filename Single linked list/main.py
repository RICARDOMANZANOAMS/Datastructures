class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None

    def prepend(self,data):
        '''
        This method append a node at the beginning of the linked list
        Args:
            data: Var that contains the data of each node
        '''
        if not self.head:
            new_node=Node(data) # create new node
            self.head=new_node  #Point the head to the new node
        else:
            new_node=Node(data)  #create new node
            new_node.next=self.head #point new_node next to the head
            self.head=new_node #move the head to the new_node

    def append(self,data):
        '''
        This method appends a new node at the end of the linked list

        '''
        if not self.head:  #check if no nodes in linked list
            new_node=Node(data) #create first node
            self.head=new_node #move head pointer to node
        else:
            cur=self.head  #Get node that it is the head
            while cur.next: #advance until reach the last node
                cur=cur.next #advance until reach next node
            new_node=Node(data) #create new node
            cur.next=new_node #point the last node next to new node
            new_node.next=None #point new node to none

    def appendNodeAtPosition(self,data,position):
        '''
        This method append a node after the position specify.
        It starts the count with 0 in the head
        '''
        if not self.head:
            new_node=Node(data)
            self.head=new_node
        else:
            cur=self.head
            cur_pos=0
            while cur_pos<=position:
                cur_pos+=1
                cur=cur.next
            new_node=Node(data)
            new_node.next=cur.next
            cur.next=new_node        






    def printNodes(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

if __name__=="__main__":
    singleLinkedListObj=SingleLinkedList()
    singleLinkedListObj.prepend(10)
    singleLinkedListObj.prepend(34)
    singleLinkedListObj.prepend(15)
    singleLinkedListObj.prepend(6)
    singleLinkedListObj.append(8)
    singleLinkedListObj.printNodes()
    singleLinkedListObj.appendNodeAtPosition(25,2)
    singleLinkedListObj.printNodes()
    
    
    
    

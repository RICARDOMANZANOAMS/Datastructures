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
    singleLinkedListObj.printNodes()
    
    
    

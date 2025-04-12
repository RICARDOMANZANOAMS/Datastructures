class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        '''
        It is similart to append because we append an element at the end not at the beginning
        '''
        new_node=Node(data)
        if self.head==None and self.tail==None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def dequeue(self):
        '''
        We pick the first element in the queue. It means the head

        '''
        data=self.head.data
        self.head=self.head.next
        return data

    def printQueue(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

if __name__=="__main__":
    queueObj=queue()
    queueObj.enqueue(1)
    queueObj.enqueue(5)
    queueObj.enqueue(34)
    queueObj.enqueue(4)
    queueObj.printQueue()
    dequeueVal=queueObj.dequeue()
    print(f'This is the dequeue value {dequeueVal}')
    queueObj.printQueue()
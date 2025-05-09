class minheap:
    def __init__(self):
        self.heap=[]

    def getParent(self,idx):
        '''
        This method finds the parent of an specific index in the list

        Args:
            idx: index to the get the parent
        '''
        if idx==0:
            return None
        else:
            parentIdx=(idx-1)//2
            return parentIdx

    def getRight(self,idx):
        '''
        This method gets the right child of the idx
        Args:
            idx: idx to get the right child of the idx
        '''
        idxRight=idx*2+2
        if idxRight>=len(self.heap):
            return None
        else:
            return idxRight
    
    def getLeft(self,idx):
        '''
        This method gets the left child of the idx
        Args:
            idx: idx to get the left child of the idx
        '''
        idxLeft=idx*2+1
        if idxLeft>=len(self.heap):
            return None
        else:
            return idxLeft
    def sifttup(self,idx):
        '''
        This method compares the value of the current idx with the parent.
        Since this is a min heap, if the value is less than the parent it passed as parent and parent as child

        '''
        idxParent=self.getParent(idx)
        while idxParent!=None and self.heap[idx]<self.heap[idxParent]:
            self.heap[idx],self.heap[idxParent]=self.heap[idxParent],self.heap[idx]
            idx=idxParent
            idxParent=self.getParent(idx)
            
    def siftDown(self,idx):
        '''
        It takes the parent node and moves the value depending of this value. 
        It moves left or right replacing the minimum value of left or right
        
        '''
        while True:
            idxLeft = self.getLeft(idx)
            idxRight = self.getRight(idx)
            idxMin = idx

            if idxLeft is not None and self.heap[idxLeft] < self.heap[idxMin]:
                idxMin = idxLeft

            if idxRight is not None and self.heap[idxRight] < self.heap[idxMin]:
                idxMin = idxRight

            if idx == idxMin:
                break
            else:
                self.heap[idx], self.heap[idxMin] = self.heap[idxMin], self.heap[idx]
                idx = idxMin
        

    def insertNode(self,val):
        '''
        This method insert a new node in the heap.
        Insertion is done at the end of the list and then the value is moving up depending 
        on the value of its parent
        '''
        self.heap.append(val)
        idx=len(self.heap)-1
        self.sifttup(idx) 

    def deleteNode(self):
        '''
        Deletes the root (minimum value) from the heap, replaces it with the last element,
        and restores the heap property by sifting down.
        
        '''
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()  

        if self.heap:  
            self.heap[0] = last
            self.siftDown(0)

        return root

    def printHeap(self):
        print(self.heap)

heapMinObj=minheap()
heapMinObj.insertNode(35)
heapMinObj.insertNode(20)
heapMinObj.insertNode(15)
heapMinObj.insertNode(10)
heapMinObj.insertNode(4)
heapMinObj.insertNode(1)
heapMinObj.printHeap()
heapMinObj.deleteNode()
val=heapMinObj.printHeap()



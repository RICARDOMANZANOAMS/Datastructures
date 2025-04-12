class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    #we have only one pointer that it is the top pointer
    def __init__(self):
        self.top=None

    def push(self,data):
        '''
        It is similar to prepend. We append before the element in the beginning.
        '''
        if self.top==None:
            new_node=Node(data)
            self.top=new_node
        else:
            new_node=Node(data)
            new_node.next=self.top
            self.top=new_node
    def pop(self):
        '''
        We discard the first element on the top of the stack
        '''
        if self.top==None:
            raise "No elements in stack"
        else:
            pop_value=self.top.data
            self.top=self.top.next

        return pop_value
    
    def pick(self):
        '''
        We look for the first element in the stack
        '''
        if self.top:
            return self.top.data
        else:
            raise "No value to pick"
    def printStack(self):
        '''
        Print the entire stack
        '''
        cur=self.top
        while cur:
            print(cur.data)
            cur=cur.next

if __name__=="__main__":
    stackObj=stack()
    stackObj.push(10)
    stackObj.push(4)
    stackObj.push(3)
    stackObj.push(11)
    stackObj.printStack()
    
    

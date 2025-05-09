class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
    def insertNode(self,data):
        if data < self.data:
            if self.left==None:
                self.left=BinaryTree(data)
            else:
                self.left.insertNode(data)
        else:
            if self.rigth==None:
                self.rigth=BinaryTree(data)
            else:
                self.rigth.insertNode(data)

bt=BinaryTree(40)
bt.insertNode(38)
bt.insertNode(37)
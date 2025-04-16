class graph:
    def __init__(self):
        self.adjancentArray=dict()

    def insertNode(self,node):
        if node not in self.adjancentArray.keys():
            self.adjancentArray[node]=[]
        else:
            print("Node already exists")
    
    def createLink(self,node1,node2,weight):
        if node1 not in self.adjancentArray.keys():
            self.insertNode(node1)
        if node2 not in self.adjancentArray.keys():
            self.insertNode(node2)
        self.adjancentArray[node1].append((node2,weight))
    def printNodesWithConnections(self):
        for k,v in self.adjancentArray.items():
            print(f'Node {k} with connection {v}')

gr=graph()
gr.createLink('A','B',10)  
gr.createLink('A','C',20)
gr.createLink('A','D',30)
gr.printNodesWithConnections()
      



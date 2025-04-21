class graph:
    def __init__(self):
        self.adjacent_matrix={}
    
    def addNode(self,nameNode):
        if nameNode not in self.adjacent_matrix:
            self.adjacent_matrix[nameNode]=[]
    def addConnection(self,node1,node2,weigth):
        if node1 not in self.adjacent_matrix:
            self.addNode(node1)
        if node2 not in self.adjacent_matrix:
            self.addNode(node2)
        self.adjacent_matrix[node1].append((node2,weigth))
        self.adjacent_matrix[node2].append((node1,weigth))
    def printGraph(self):
        for key,val in self.adjacent_matrix.items():
            print(key)
            print(val)
    def shortestpath(self,node1,node2):
        nodes=self.adjacent_matrix.keys()
        predecesor={}
        costs={}
        for node in nodes:
            predecesor[node]=None
            if node==node1:
                costs[node]=0
            else:
                costs[node]=999
        print(predecesor)
        print(costs)

        for actualNode,neighbors in self.adjacent_matrix.items():
            for neighborkey,weight in neighbors:
                if (costs[actualNode]+weight)<costs[neighborkey]:
                    costs[neighborkey]=costs[actualNode]+weight
                    predecesor[neighborkey]=actualNode

        print(predecesor)
        print(costs)
        print("shortest path")
        print(node2)
        result=predecesor[node2]
        while result!=node1:
            print(result)
            result=predecesor[result]
        print(node1)
            



        


gp=graph()
gp.addConnection('A','B',10)
gp.addConnection('A','C',5)
gp.addConnection('A','D',20)
gp.addConnection('B','E',10)
gp.addConnection('C','E',15)
gp.addConnection('C','D',4)
gp.addConnection('C','F',20)
gp.addConnection('D','F',5)
gp.addConnection('F','E',2)
gp.addConnection('F','G',10)
gp.addConnection('E','G',3)

gp.printGraph()
gp.shortestpath('B','D')

class graph_structure:
    def __init__(self):
        self.sq = [[" "," "],[" "," "]]
        
    def edge(self,Node):
        temp = self.sq[0]
        if self.sq[0][-1] != " ":
            self.sq[0].append(" ")
            First = False
        else:
            First = True
        check = 0
        if self.sq[0][0] == " ":
            self.sq[0][0] = "-"
        for i in range (len(self.sq[0])):
            if i == len(self.sq[0])- 1 and not First:
                self.sq.append([])
            while len(self.sq[i]) < len(self.sq[i-1]):
                self.sq[i].append("0")
                if self.sq[i][0] == "0":
                    self.sq[i][0] = " "
        for i in range (len(self.sq)):
            if self.sq[0][i] == " " and check == 0:
                self.sq[0][i] = Node
                check = 1
        for j in range (len(self.sq[0])):
            if self.sq[j][0] == " " and check == 1:
                self.sq[j][0] = Node
                self.sq[j][1] = "0"
                check = 0
                
    def Adj_matrix(self):
        print(len(self.sq) * "=")
        for i in range(len(self.sq)):
            print(self.sq[i])
            
    def con_Node(self,Node_one,Node_two):
        if Node_one in self.sq[0] and Node_two in self.sq[0] :
            Node_oneIndex,Node_twoIndex = 0,0
            for i in range(len(self.sq)):
                if Node_one == self.sq[0][i]:
                    Node_oneIndex = i
                elif Node_two == self.sq[0][i]:
                    Node_twoIndex = i
            self.sq[Node_oneIndex][Node_twoIndex] = "1"
            self.sq[Node_twoIndex][Node_oneIndex] = "1"
        else:
            print ("is Not")
            
    def Adj_List(self):
        temp_List = [ ]
        for i in range(1,len(self.sq)):
            temp_List.append(str(self.sq[i][0]) + ":")
            for j in range(1,len(self.sq)):
                if self.sq[i][j] == "1":
                    temp_List.append(self.sq[0][j])
            print(temp_List)
            temp_List=[]
            
    def edge_List(self):
        temp_List = [ ]
        List = [ ]
        output = [[ ],[ ]]
        for i in range(1,len(self.sq)):
            temp_List.append(str(self.sq[i][0]) + ":")
            List.append(self.sq[i][0])
            for j in range(1,len(self.sq)):
                if self.sq[i][j] == "1":
                    temp_List.append(self.sq[0][j])
                    check = len(List)
                    List[check-1] += self.sq[0][j]
                    if j != (len(self.sq) - 1):
                        List.append(self.sq[i][0])
                elif (j == (len(self.sq) - 1) and self.sq[i][j] == "0"):
                    List.pop()
            temp_List=[ ]
        count = 0
        for i in range(len(List)):
            Get = List.pop(0)
            if Get[::-1] not in output[1]:
                output[0].append(str(count) + ":")
                output[1].append(Get)
                count += 1
        for i in range (len(output[0])):
            print(str(output[0][i]) + " " + str(output[1][i]))

graph = graph_structure()
graph.edge("A")
graph.edge("B")
graph.edge("C")
graph.edge("D")
graph.edge("E")
graph.edge("F")
graph.con_Node("A","B")
graph.con_Node("A","C")
graph.con_Node("A","F")
graph.con_Node("C","D")
graph.con_Node("D","E")
graph.con_Node("E","F")
graph.Adj_matrix()
graph.Adj_List()
graph.edge_List()

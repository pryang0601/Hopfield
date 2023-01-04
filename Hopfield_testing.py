import numpy as np
import copy
class Hopfield_Test:
    def __init__(self,Data,Hop):
        self.Data=Data
        self.weight=Hop.weight
        self.thetas=Hop.thetas
        self.row_num=Hop.row_num
        self.col_num=Hop.col_num
        self.X=np.zeros(self.row_num*self.col_num).astype(int)
        self.test_graph=self.test_transform(count=0,data=self.Data)
        self.train_graph=self.test_transform(count=0,data=Hop.Data)
        self.epoch=200
    def test_transform(self,count,data):
        graph=[]
        for i in range(len(data)): 
            column_len=len(data[i])
            if((i+1)%(self.row_num+1)!=0):
                for j in range(column_len):
                    if(data[i][j]==' '):
                        self.X[count]=-1
                    else:
                        self.X[count]=1
                    count+=1
            if((i+1)%(self.row_num+1)==0 or i==len(data)-1):
                count=0
                tmp=copy.copy(self.X)
                graph.append(tmp)
        return graph
    def train(self):
        for i in range(len(self.test_graph)):
            comparsion=np.copy(self.test_graph[i])
            for r in range(self.epoch):
                for j in range(self.weight.shape[0]):
                    tmp=np.dot(self.weight[j].reshape(1,-1),comparsion.reshape(-1,1))
                    if(tmp>self.thetas[j]):
                        comparsion[j]=1
                    elif(tmp<self.thetas[j]):
                        comparsion[j]=-1
                if((comparsion==self.train_graph[i]).all()):
                    break
            self.test_graph[i]=comparsion
    
    def print_test(self):
        with open("print_after.txt","w") as f:
            for graph in self.test_graph:
                idx=0
                for r in graph:
                    if(r==1):
                        f.write("1")
                    else: 
                        f.write(" ")
                    idx+=1
                    if(idx%self.col_num==0):
                        f.write("\n")
                        idx=0
                f.write("\n")
import numpy as np
class Hopfield_Train:
    def __init__(self,Data,row_num,col_num):
        self.Data=Data
        self.graph=[]
        self.input_num=0
        self.row_num,self.col_num=row_num,col_num
        self.X=np.zeros(self.row_num*self.col_num).astype(int)
        self.y=np.zeros(self.row_num*self.col_num)
        self.weight=self.compute_weight(count=0)
        self.thetas=self.regularize()
        self.results=self.compute_y()
    def compute_weight(self,count):
        weight=np.zeros((self.row_num*self.col_num,self.row_num*self.col_num))
        X=np.zeros(self.row_num*self.col_num).astype(int)
        for i in range(len(self.Data)):             #transform the graph to (-1,1)
            if((i+1)%(self.row_num+1)!=0):
                for j in range(self.col_num):
                    if(self.Data[i][j]==' '):                       
                        X[count]=-1
                    else:
                        X[count]=1
                    count+=1
            if( (i+1)%(self.row_num+1)==0 or i==len(self.Data)-1):
                self.input_num+=1
                count=0
                self.graph.append(X.reshape(-1,1))                   #change to column vector
                w=np.dot(X.reshape(-1,1),X.reshape(1,-1))
                X=np.zeros(self.row_num*self.col_num).astype(int)      #x change to original form
                weight=np.add(weight,w)                         #total weight
        
        return weight
    def regularize(self):
        self.weight=self.weight/(self.row_num*self.col_num)-(self.input_num/(self.row_num*self.col_num))*np.identity(self.row_num*self.col_num)         #regularize
        thetas=np.zeros(self.row_num*self.col_num)
        return thetas
    def compute_y(self):
        results=[]
        for g in self.graph:
            y=np.dot(self.weight,g)
            y=np.round(y,4)
            tmp=[]
            for i in range(y.shape[0]):
                if(y[i]>self.thetas[i]):
                    tmp.append(1)
                elif(y[i]==self.thetas[i]):
                    tmp.append(g[i])
                else:
                    tmp.append(-1)
            results.append(tmp)
        return results
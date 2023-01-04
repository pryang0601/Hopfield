###把訓練資料加入雜訊
import random
import numpy as np
with open("Bonus_Training.txt") as f1:
    train_data=f1.read().splitlines()
for i in range(len(train_data)):         #get the matrix shape
    col_num=len(train_data[i])
    if(col_num==0):
        row_num=i
        col_num=len(train_data[i+1])
        break
                                             #0 : don't change
X=np.zeros(row_num*col_num).astype(int)
graph=[]
count=0
for i in range(len(train_data)):             #transform the graph to (-1,1)
    if((i+1)%(row_num+1)!=0):
        for j in range(col_num):
            c=np.random.choice([1, 0], p=[0.25, 0.75])
            if((train_data[i][j]==' ' and c==0) or (train_data[i][j]=='1' and c==1)):
                X[count]=-1
            elif((train_data[i][j]=='1' and c==0) or (train_data[i][j]==' ' and c==1)):
                X[count]=1
            count+=1
    if( (i+1)%(row_num+1)==0 or i==len(train_data)-1):
        count=0
        graph.append(X.reshape(-1,1))                   #change to column vector
        X=np.zeros(row_num*col_num).astype(int)      #x change to original form
change=""
for tmp in graph:
    idx=0
    for r in tmp:
        if(r==1):
            change+="1"
            # print("1",end="")
        else: 
            change+=" "
            # print(" ",end="")
        idx+=1
        if(idx%col_num==0):
            change+='\n'
            idx=0
    change+='\n'
with open("Bonus_Change_Testing.txt","w") as f:
    f.write(change)
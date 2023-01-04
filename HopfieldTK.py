import tkinter as tk
from tkinter import ttk,font
import tkinter.scrolledtext as st
from Hopfield_training import Hopfield_Train
from Hopfield_testing import Hopfield_Test
class GUI():
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('700x600')
        self.root.title("HOPFIELD")
        self.trainData=ttk.Label(self.root,text="Train Data",font="Times 14 bold")
        self.trainData.grid(row=0,column=0,ipadx=5,ipady=5)
        self.testData=ttk.Label(self.root,text="Test Data",font="Times 14 bold")
        self.testData.grid(row=0,column=1,ipadx=5,ipady=5)
        self.selected_train=tk.StringVar()
        self.trainSet=ttk.Combobox(self.root,textvariable=self.selected_train)
        self.trainSet['value']=['Basic_Training.txt','Bonus_Training.txt']
        self.trainSet['state']='readonly'
        self.trainSet.grid(row=1,column=0,ipadx=5,ipady=5)
        self.selected_test=tk.StringVar()
        self.testSet=ttk.Combobox(self.root,textvariable=self.selected_test)
        self.testSet['value']=['Basic_Testing.txt','Bonus_Testing.txt','Basic_Change_Testing.txt','Bonus_Change_Testing.txt']
        self.testSet.grid(row=1,column=1,ipadx=5,ipady=5)
        self.start=ttk.Button(self.root,text="Start Training",command=lambda:self.train(self.selected_train.get(),self.selected_test.get()))
        self.start.grid(row=1,column=2)
        self.before=st.ScrolledText(self.root,width=30)
        self.before.grid(row=3,column=1)
        self.after=st.ScrolledText(self.root,width=30)
        self.after.grid(row=3,column=2)
        self.trainDataText=st.ScrolledText(self.root,width=30)
        self.trainDataText.grid(row=3,column=0)
        self.beforeLabel=ttk.Label(self.root,text="Data before Training",font="Times 14 bold")
        self.beforeLabel.grid(row=2,column=1,ipadx=5,ipady=5)
        self.afterLabel=ttk.Label(self.root,text="Data after Training",font="Times 14 bold")
        self.afterLabel.grid(row=2,column=2,ipadx=5,ipady=5)
        self.trainLabel=ttk.Label(self.root,text="Training Data",font="Times 14 bold")
        self.trainLabel.grid(row=2,column=0,ipadx=5,ipady=5)
        self.reset=ttk.Button(self.root,text="Reset",command=lambda:self.RESET())
        self.reset.grid(row=4,column=1)
        
        self.root.mainloop()
    def RESET(self):
        self.trainDataText.delete('1.0',tk.END)
        self.before.delete('1.0',tk.END)
        self.after.delete('1.0',tk.END)
    def train(self,TrainDataset,TestDataset):
        with open(f"{TestDataset}","r") as f1:
            test_data=f1.read().splitlines()
        for num in test_data:
            for n in num:
                if n=='1':
                    self.before.insert(tk.END,"1")
                else:
                    self.before.insert(tk.END," ")
            self.before.insert(tk.END,'\n')
        with open(f"{TrainDataset}","r") as f2:
            train_data=f2.read().splitlines()
        for num in train_data:
            for n in num:
                if n=='1':
                    self.trainDataText.insert(tk.END,"1")
                else:
                    self.trainDataText.insert(tk.END," ")
            self.trainDataText.insert(tk.END,'\n')
        if TrainDataset=='Basic_Training.txt':
            H_train=Hopfield_Train(train_data,12,9)
        elif TrainDataset=='Bonus_Training.txt':
            H_train=Hopfield_Train(train_data,10,10)
        elif TrainDataset=='number.txt':
            H_train=Hopfield_Train(train_data,10,9)
        h_test=Hopfield_Test(test_data,H_train)
        h_test.train()
        h_test.print_test()
        with open("print_after.txt","r") as f1:
            test_after=f1.read().splitlines()
        for num in test_after:
            for n in num:
                if n=='1':
                    self.after.insert(tk.END,"1")
                else:
                    self.after.insert(tk.END," ")
            self.after.insert(tk.END,'\n')
if __name__=='__main__':
    g=GUI()
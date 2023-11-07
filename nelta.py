"""
Add LabeledList and Table classes
"""

class LabeledList:
    def __init__(self, data=None, index=None):
        self.values=data
        if(index==None):
            self.index=[i for i in range(0,len(data),1)]
        else:
            self.index=index
            
    def __str__(self):
        string=''
        for i,j in zip(self.values, self.index):

            string+=f'{str(j)}{str(i):>10}'+'\n'
        return string
            
    
    def __repr__(self):
        return self.__str__()
    
    
    
    def __getitem__(self, key_list):
        dex=[]
        value=[]
        for index, i in enumerate(key_list):
            if (type(i)==bool):
                if(i==True):
                    dex.append(self.index[index])
                    value.append(self.values[index])
            else:
                for indexj, j in enumerate(self.index):
                    if(i==j):
                        dex.append(i)
                        value.append(self.values[indexj])
        return LabeledList(value,dex)
                    
    def __iter__(self):
        return iter(self.values)        
    
    def __eq__(self, scalar):
        dex=[]
        value=[]
        for i,index in zip(self.values,self.index):
            if(i==scalar):
                dex.append(index)
                value.append(True)
            elif(i==None):
                dex.append(index)
                value.append(False)
            else:
                dex.append(index)
                value.append(False)
        return LabeledList(value,dex)
           
            
            
            
            
            
            
    def __ne__(self, scalar):
        dex=[]
        value=[]
        for i,index in zip(self.values,self.index):
            if(i!=scalar):
                dex.append(index)
                value.append(True)
            elif(i==None):
                dex.append(index)
                value.append(False)
            else:
                dex.append(index)
                value.append(False)
        return LabeledList(value,dex)
    def __gt__(self, scalar):
        dex=[]
        value=[]
        for i,index in zip(self.values,self.index):
            if(i>scalar):
                dex.append(index)
                value.append(True)
            elif(i==None):
                dex.append(index)
                value.append(False)
            else:
                dex.append(index)
                value.append(False)
        return LabeledList(value,dex)
    def __lt__(self, scalar):
        dex=[]
        value=[]
        for i,index in zip(self.values,self.index):
            if(i<scalar):
                dex.append(index)
                value.append(True)
            elif(i==None):
                dex.append(index)
                value.append(False)
            else:
                dex.append(index)
                value.append(False)
        return LabeledList(value,dex)
    def map(self, f):
        dex=[]
        value=[]
        for i,index in zip(self.values,self.index):
            dex.append(index)
            value.append(f(i))
        return LabeledList(value,dex)

import csv
def read_csv(fn):
    with open(fn) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data=[]
        for row in csv_reader:
            if line_count == 0:
                header=row
                line_count += 1
            else:
                row[-2]=float(row[-2])
                data.append(row)
    return Table(data=data,columns=header)

class Table:
    def __init__(self, data, index=None, columns=None):
        self.values=data
        if(index==None):
            self.index=[i for i in range(0,len(data),1)]
        else:
            self.index=index
            
        if(columns==None):
            self.columns=[i for i in range(0,len(data[0]),1)]
        else:
            self.columns=columns
            
    def __str__(self):
        string=' '
        for k in self.columns:
            string+=f'{str(k):>9}'
        string+='\n'
        for indexi,i in enumerate(self.index):
            string+='\n'
            string+=str(i)
            for indexj,j in enumerate(self.columns):
                string+=f'{str(self.values[indexi][indexj]):>10}'
        return string
            
    
    def __repr__(self):
        return self.__str__()
    
    
    
    def __getitem__(self, col_list):
        data=[]
        dex=[]
        col=[]
        if isinstance(col_list,str):
            if (self.columns.count(col_list)==1):
                for indexj,j in enumerate(self.columns):
                    if(col_list==j):
                        for indexk, k in enumerate(self.index):
                            data.append(self.values[indexk][indexj])
                return LabeledList(data=data,index=self.index)
        
            else:
                
                
                for indexj,j in enumerate(self.columns):
                    if(j==col_list):
                        col.append(j)
                        line=[]
                        for indexk, k in enumerate(self.index):
                            line.append(self.values[indexk][indexj])
                        data.append(line)
                
                return Table(data,self.index,col)
                        
                
        
        if isinstance(col_list,LabeledList):
            col_list=col_list.values
            
        if  all((isinstance(i,bool) for i in col_list)):
            col=self.columns
            for j in range(len(col_list)):
                if(col_list[j]==True):
                    data.append(self.values[j])
                    dex.append(self.index[j])
            return Table(data,dex,self.columns)
        else:
        
            for indexk, k in enumerate(self.index):
                line=[]
                for indexj,j in enumerate(self.columns):
                    for i in col_list:
                        if(i==j):
                            col.append(i)
                            line.append(self.values[indexk][indexj])
                            
                data.append(line)  
            return Table(data,self.index,col_list)
        

                    
    def head(self, n):
        return Table(self.values[:n],self.index[:n],self.columns)
        
    def tail(self, n):
        return Table(self.values[len(self.index)-n:],self.index[len(self.index)-n:],self.columns)
        
    def shape(self):
        return (len([i for i in self.index]),len(self.columns))
    
 
            
        
        

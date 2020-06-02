import numpy as np
import pandas as pd
import math
import operator

test=[[170,55,'Female'],[145,56,'Male']]
k=5
res=[]
f=pd.read_csv('C:\Python\Python38\Data Science\\tshirt_size.csv')
def eud(x,y,t):
	a=[0]*len(x)
	s=0
	for i in range(len(x)):
		
		
		s=math.pow((t[0]-x[i]),2)+math.pow((t[1]-y[i]),2)
		a[i]= math.sqrt(s)
	return a
def find_nearest_neighbor(x):
        neighbors={'Male':0,'Female':0}
        for i in range(k):
                if neighbors[x[i][0]]==0:
                        neighbors.update({x[i][0]:1})
                else:
                        neighbors.update({x[i][0]:neighbors[x[i][0]]+1})
        
        
        return max(neighbors,key=neighbors.get)
         
        
def find_accuracy():
        c=0
        for i in range(len(test)):
               if test[i][-1] is res[i]:
                       c+=1
        return c/len(test)*100

for i in range(len(test)):
        x=eud(f['Height'],f['Weight'],test[i])
        f['dis']=x
        ds=np.array(f)
        for j in range(k):
                print("nearest neighbors for"+str(i)+"test data"+ str(ds[j]))
        ds=sorted(ds,key=operator.itemgetter(3))
        res.append( find_nearest_neighbor(ds))
        
print("predicted value"+ str(res))
print("accuracy",find_accuracy())


        
        

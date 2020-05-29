import numpy as np
import pandas as pd

import matplotlib.pyplot as py
x=np.array([1,2,3,4,5])
y=np.array([3,4,2,4,5])
def predictx(x,y):
	m=0
	u=0
	d=0
	x_bar=x.sum()/len(x)
	y_bar=y.sum()/len(y)
	for i in range(len(x)):
		try:
			u=u+(x[i]-x_bar)*(y[i]-y_bar)
			d=d+((x[i]-x_bar)*(x[i]-x_bar))
			m=u/d
		except:
			m=m+0
			
	c=y_bar-(m*x_bar)
	yp=[0]*len(x)
	for i in range(len(x)):
		yp[i]=m*x[i]+c

	up=0
	down=0
	for i in range(len(x)):
		up=up+(yp[i]-y_bar)*(yp[i]-y_bar)
		down=down+(y[i]-y_bar)*(y[i]-y_bar)
	r=up/down
	print("x_bar",x_bar)
	print("y_bar",y_bar)
	print("m value",m)
	print("y predicted",yp)
	print("R2",r)
	py.scatter(x,y,label="Scatter")
	py.plot(x,yp,label="Regression line")
	py.xlabel("x Values")
	py.ylabel("y values")
	py.show()   
predictx(x,y)

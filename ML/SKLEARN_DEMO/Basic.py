from sklearn import datasets
from sklearn.model_selection import  train_test_split
import numpy as np


irisdataset =datasets.load_iris()

x=irisdataset.data

y=irisdataset.target

print(f" x={x.shape} \nY={y.shape}")# x=150row and 4 col and Y=150 rows and 1col

#splite DataSet test size and trian size

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2);



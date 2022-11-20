import pandas as pd
from sklearn import preprocessing

dataset =pd.read_csv('../DATA/CAR/USA_cars_datasets.csv')


X=pd.DataFrame(dataset,columns=[ 'model','state' ,'brand', 'year'])
print(X)

Y=pd.DataFrame(dataset,columns=['price'])
print(Y)


#print(model.predict(['cruiser','new jersey',' toyota ','2018']))
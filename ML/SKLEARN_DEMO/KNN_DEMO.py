
#knn = k  nearest Neighbour
#most try to use K =odd NUmber

#example used in-------------------> recommendation system uses knn<--------------------------------------------------
# also used in concept search
from sklearn import neighbors
from sklearn import datasets
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report

dataset=datasets.load_iris()

x=dataset.data
y=dataset.target

print(f'x shape ={x.shape} \ny shape ={y.shape}')

model=KNeighborsClassifier(n_neighbors=10)

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2)

model.fit(x_train,y_train)
Y_OUT=model.predict(x_test)
print(f'model prediction : {model.predict(x_test)}')

print(f'accuracy score :{accuracy_score(y_test,Y_OUT)}')

print(f'classification report:{classification_report(y_test,Y_OUT)}')

k=neighbors.kneighbors_graph(model,n_neighbors=10,mode='connectivity', metric='minkowski')

print(k)
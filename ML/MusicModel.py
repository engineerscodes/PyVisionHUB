import  pandas as pd



music=pd.read_csv("./DATA/music.csv")

print(music)
print(music.shape)
print(music.describe())

"""  this data set has not null value 
all  18 rows have value look at count...
             age     gender
count  18.000000  18.000000  
mean   27.944444   0.500000
std     5.127460   0.514496
min    20.000000   0.000000
25%    25.000000   0.000000
50%    28.000000   0.500000
75%    31.000000   1.000000
max    37.000000   1.000000

"""

#Now divide the data set into two set (one input set and outputset  to train model)
#let input set be age and gender and output set be Genre
#now take input from user age and gender and predict the output genre

#using drop remove genre form input set
#x=input dataset
print("================================input dataSet============================================================")
x=music.drop(columns=['genre'])
print(x)

#y=output data set
#u should only have genre column or u can drop age amd gender colunm

# y=music.drop(columns=['age','gender']) or
y=music['genre']
print(y)

#now select a algo to find output each algo has advantages and disadvantages
#let use dicision Tree Simple one using skLearn

from sklearn.tree  import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
model=DecisionTreeClassifier()

model.fit(x,y)
#pass input set [[age1,gender1],[age2,gender2]] 2d input array
predictions =model.predict([[21,1],[22,0]])

print(predictions)
print("=======================measure predictions/cal accuracy===================")
#to measure accuracy u did to divide into 2 part test and train set
#mostly train 70%-80% and test 30%-20%
 #return a tuple and u can unpack into 4 (xtrain,xtest)input set and outset(ytrain ,ytest)
 #it randomly slit data in any order
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #take input and output and size of test set=0.2 =20%
#now pass only train model set to fit or learn
model.fit(x_train,y_train)
#and pass test to predict
test_predictions=model.predict(x_test)
print(test_predictions)
#use accuracy sore compare y_test with test_perdictions

score=accuracy_score(y_test,test_predictions)

print(score)
#score changes from 0.75 -1.0 because to random slit of dataset

#testing with multiple testsize letstake 80%

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8) #take input and output and size of test set=0.2 =20%
#now pass only train model set to fit or learn
model.fit(x_train,y_train)
#and pass test to predict
test_predictions=model.predict(x_test)
print(test_predictions)
#use accuracy sore compare y_test with test_perdictions

score=accuracy_score(y_test,test_predictions)

print(f"SCORE THE TEST SIXE 80% :{score}") # the accuracy_score drop to 0.26666666666666666
#so for training set u need more data


#save the model and read the trained model later
#from sklearn.externals import joblib
'''Python37\lib\site-packages\sklearn\externals\joblib_init_.py:15: DeprecationWarning: 
sklearn.externals.joblib is deprecated in 0.21 and will be removed in 0.23. Please import this functionality directly 
from joblib, which can be installed with: pip install joblib. 
If this warning is raised when loading pickled models, you may need to re-serialize those models with scikit-learn 0.21+.'''
import  joblib

joblib.dump(model ,'music_model.joblib')








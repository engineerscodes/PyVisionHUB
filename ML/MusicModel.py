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

model=DecisionTreeClassifier()

model.fit(x,y)
#pass input set [[age1,gender1],[age2,gender2]] 2d input array
predictions =model.predict([[21,1],[23,0]])

print(predictions)






import pandas as pd
from sklearn import tree
from sklearn.tree  import DecisionTreeClassifier

music=pd.read_csv("./DATA/music.csv")

print(music)
print(music.shape)
print(music.describe())


print("================================input dataSet============================================================")
x=music.drop(columns=['genre'])
print(x)

y=music['genre']
print(y)

model=DecisionTreeClassifier()

model.fit(x,y)





tree.export_graphviz(model,out_file="music_Dtree_naveen.dot",feature_names=['age','gender'],class_names=sorted(y.unique()),label='all',
                     rounded=True,filled=True
                     )


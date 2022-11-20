import  pandas as pd

dataset= pd.read_csv(".//DATA//vgsales.csv")

print(dataset)

print(dataset.shape)

print(dataset.describe())

print(dataset.values)



import  numpy as np


irisdataset=np.genfromtxt('iris.txt',skip_header=1, delimiter=',', dtype = float)

print(irisdataset.shape)
#we have 30 rows and 6 col
print(f'2 D Array \n{irisdataset}')
#drop 4th clounm beacuse its has nan values

irisdataset=irisdataset[:,[0,1,2,3,5]] #sliceing the array
print(f'2 D Array after removing 4 clounm \n{irisdataset}')

print(f"new shape after dropping col 4 ---->{irisdataset.shape}\nnew dimensions are ---->{irisdataset.ndim}"
      f"\nand new size ---->{irisdataset.size}")

iris1, iris2, iris3 = np.split(irisdataset, [10,20], axis=0)
print(f"IRIS1 \n{iris1}\nIRIS2\n{iris2}\nIRIS3\n{iris3}")

iris_header=np.array(["sepal length", "sepal width", "petal length", "petal width","Species No"],dtype=str)
print(f"HEADER --->{iris_header}")

#print max of each col

iris_max=irisdataset.max(axis=0).round(2)
iris_min=irisdataset.min(axis=0).round(2)
iris_avg=irisdataset.mean(axis=0).round(2)
iris_std=irisdataset.std(axis=0).round(2)
iris_var=irisdataset.var(axis=0).round(2)
print(f'max values---->{iris_max}\nmin values ----->{iris_min}\nMean of each col ---->{iris_avg}'
      f'\nstd of each col --->{iris_std} \nvar of each col --->{iris_var}')
iris1_max=iris1.max(axis=0).round(2)
iris1_min=iris1.min(axis=0).round(2)
iris1_avg=iris1.mean(axis=0).round(2)
iris1_std=iris1.std(axis=0).round(2)
iris1_var=iris1.var(axis=0).round(2)
print(f'STATC FOR IRIS 1 \nmax values---->{iris1_max}\nmin values ----->{iris1_min}\nMean of each col ---->{iris1_avg}'
      f'\nstd of each col --->{iris1_std} \nvar of each col --->{iris1_var}')

iris2_max=iris2.max(axis=0).round(2)
iris2_min=iris2.min(axis=0).round(2)
iris2_avg=iris2.mean(axis=0).round(2)
iris2_std=iris2.std(axis=0).round(2)
iris2_var=iris2.var(axis=0).round(2)
print(f'STATC FOR IRIS 2 \nmax values---->{iris2_max}\nmin values ----->{iris2_min}\nMean of each col ---->{iris2_avg}'
      f'\nstd of each col --->{iris2_std} \nvar of each col --->{iris2_var}')


iris3_max=iris3.max(axis=0).round(2)
iris3_min=iris3.min(axis=0).round(2)
iris3_avg=iris3.mean(axis=0).round(2)
iris3_std=iris3.std(axis=0).round(2)
iris3_var=iris3.var(axis=0).round(2)
print(f'STATC FOR IRIS 3 \nmax values---->{iris3_max}\nmin values ----->{iris3_min}\nMean of each col ---->{iris3_avg}'
      f'\nstd of each col --->{iris3_std} \nvar of each col --->{iris3_var}')

print("#########     sepal length         #############################")
print(f"min sepal length of (Iris-setosa) Vs the min sepal -->{iris1_min[0]>iris_min[0]}")
print(f"min sepal length of Iris-versicolor Vs the min sepal -->{iris2_min[0]>iris_min[0]}")
print(f"min sepal length of Iris-virginica Vs the min sepal -->{iris3_min[0]>iris_min[0]}")
print("#########     sepal width         #############################")
print(f"min sepal width of (Iris-setosa) Vs the min sepal -->{iris1_min[1]>iris_min[1]}")
print(f"min sepal width of Iris-versicolor Vs the min sepal -->{iris2_min[1]>iris_min[1]}")
print(f"min sepal width of Iris-virginica Vs the min sepal -->{iris3_min[1]>iris_min[1]}")

print("#########     petal length         #############################")
print(f"min petal length of (Iris-setosa) Vs the min sepal -->{iris1_min[2]>iris_min[2]}")
print(f"min petal length of Iris-versicolor Vs the min sepal -->{iris2_min[2]>iris_min[2]}")
print(f"min petal length of Iris-virginica Vs the min sepal -->{iris3_min[2]>iris_min[2]}")


print("#########     petal width        #############################")
print(f"min petal width of (Iris-setosa) Vs the min sepal -->{iris1_min[3]>iris_min[3]}")
print(f"min petal width of Iris-versicolor Vs the min sepal -->{iris2_min[3]>iris_min[3]}")
print(f"min petal width of Iris-virginica Vs the min sepal -->{iris3_min[3]>iris_min[3]}")

print()
print(f"Compare Iris setosa’s average sepal width to that of Iris virginica (iris setosa> IRIS VIRGINICA)"
      f"---> {iris1_avg[1] > iris2_avg[1]}")

print(f"Compare Iris setosa’s average petal length to that of Iris virginica (iris setosa> IRIS VIRGINICA)"
      f"---> {iris1_avg[2] > iris2_avg[2]}")

print(f"Compare Iris setosa’s average petal width to that of Iris virginica (iris setosa> IRIS VIRGINICA)"
      f"---> {iris1_avg[3] > iris2_avg[3]}")